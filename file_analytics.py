"""
file_analytics.py
Generic upload -> extract -> chart pipeline for CSV, XLSX/XLS and PDF files.
"""
import io
import pandas as pd
import plotly.express as px


def load_tabular_file(uploaded_file):
    """Load a CSV or Excel upload into a DataFrame. Returns (df, message)."""
    name = uploaded_file.name.lower()
    try:
        if name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif name.endswith(".xlsx") or name.endswith(".xls"):
            df = pd.read_excel(uploaded_file)
        else:
            return None, f"Unsupported tabular format: {name}"
        return df, f"Loaded {len(df)} rows x {len(df.columns)} columns from {uploaded_file.name}."
    except Exception as e:
        return None, f"Failed to read {uploaded_file.name}: {e}"


def extract_pdf_content(uploaded_file):
    """
    Extract text and any detected tables from a PDF using pdfplumber.
    Returns dict: {"text": str, "tables": [DataFrame, ...], "message": str}
    If the PDF appears to have no extractable text (scanned/image PDF),
    flags that OCR (pytesseract + pdf2image) would be needed.
    """
    result = {"text": "", "tables": [], "message": ""}
    try:
        import pdfplumber
    except ImportError:
        result["message"] = "pdfplumber not installed."
        return result

    try:
        uploaded_file.seek(0)
        with pdfplumber.open(uploaded_file) as pdf:
            all_text = []
            all_tables = []
            for page in pdf.pages:
                t = page.extract_text() or ""
                all_text.append(t)
                for tbl in page.extract_tables():
                    if tbl and len(tbl) > 1:
                        try:
                            df = pd.DataFrame(tbl[1:], columns=tbl[0])
                            all_tables.append(df)
                        except Exception:
                            continue
            result["text"] = "\n".join(all_text)
            result["tables"] = all_tables

        if not result["text"].strip() and not result["tables"]:
            result["message"] = ("No extractable text/tables found - this PDF is likely scanned/image-based. "
                                  "OCR pathway (pytesseract + pdf2image, requires poppler installed) would be "
                                  "needed to extract data from it.")
        else:
            result["message"] = f"Extracted {len(result['text'])} characters of text and {len(result['tables'])} table(s)."
    except Exception as e:
        result["message"] = f"PDF extraction error: {e}"
    return result


def detect_numeric_columns(df):
    return [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])]


def clean_dataframe(df):
    """Basic cleaning: drop fully-empty rows/cols, strip whitespace in headers, coerce numerics where possible."""
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]
    df = df.dropna(how="all").dropna(axis=1, how="all")
    for c in df.columns:
        if df[c].dtype == object:
            coerced = pd.to_numeric(df[c].astype(str).str.replace(",", ""), errors="coerce")
            if coerced.notna().mean() > 0.7:
                df[c] = coerced
    return df


def to_csv_bytes(df):
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    return buf.getvalue().encode("utf-8")


def make_chart(df, chart_type, x_col=None, y_col=None, color_col=None, title=""):
    """Build a plotly figure of the requested type from a DataFrame + user-selected columns."""
    if chart_type == "Bar chart":
        fig = px.bar(df, x=x_col, y=y_col, color=color_col, title=title)
    elif chart_type == "Pie chart":
        fig = px.pie(df, names=x_col, values=y_col, title=title)
    elif chart_type == "Scatter plot":
        fig = px.scatter(df, x=x_col, y=y_col, color=color_col, title=title)
    elif chart_type == "Line chart":
        fig = px.line(df, x=x_col, y=y_col, color=color_col, title=title)
    else:
        fig = px.bar(df, x=x_col, y=y_col, title=title)
    fig.update_layout(margin=dict(l=10, r=10, t=40, b=10))
    return fig
