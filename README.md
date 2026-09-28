# Pakistan Water, Terrain & Risk Dashboard

**Creator:** Engr. Syed Hassan Iqbal Shah

A Streamlit dashboard covering Pakistan's provinces/territories, river systems, dams/barrages/link
canals, lakes, deserts, climate regions, mountain ranges, forests, national parks, national disaster
risk context, socio-economic & agro-economic indicators, geo-political/strategic water issues
(CPEC hydropower, inter-provincial disputes, the Indus Waters Treaty dispute), and ESG/ISO/SDG/MDG/
Vision 2030 linkages — plus a file-analytics module that turns your own uploaded CSV/XLSX/PDF data
into charts and maps.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Open the URL Streamlit prints (usually http://localhost:8501).

## Project structure

| File | Purpose |
|---|---|
| `app.py` | Main Streamlit app: sidebar navigation, all pages/tabs |
| `data_loader.py` | All static reference datasets (provinces, rivers, dams, lakes, deserts, mountains, forests, parks, hazards, crop seasons, CPEC hydropower, references) |
| `coordinates.py` | Lat/lon lookup tables for map rendering |
| `map_view.py` | Folium map builders, incl. auto-detecting lat/lon columns in uploaded data |
| `network_view.py` | Plotly/networkx river-confluence and link-canal network diagrams |
| `hydraulic_model.py` | Heuristic risk-index engine, synthetic GLOF hydrograph simulator, telemetry-variance analysis |
| `file_analytics.py` | CSV/XLSX/PDF upload, extraction, cleaning, and chart-building utilities |
| `geopolitics.py` | Indus Waters Treaty dispute content (framed as reported positions/claims with sources) |
| `sdg_module.py` | ESG / ISO / UN SDG / MDG / Vision 2030 reference mapping |
| `indus_delta.py` | Findings from Siyal & Hashmi (2019), *Impact of Climate Change in the Indus River Delta and Coastal Region of Pakistan* (GCISC-funded study) — soil salinity, Kotri Barrage flow history, sea-level rise, LECZ/coastal-inundation risk, economic loss estimates, recommendations |
| `telemetry_network.py` | WAPDA's flood-forecasting telemetry & communications network (Meteorburst system, HF Radio — Western Rivers, Wireless Network — Eastern Rivers) plus the Indus Waters Treaty reference map's barrage/link-canal list |
| `requirements.txt` | Python dependencies |

## Notes on data quality

Most datasets here are **representative/educational starting points**, not verified operational
data. Before using this for planning, reporting, or public-facing decisions, validate figures
against primary sources: WAPDA, IRSA, PMD, PCA (pca-cpa.org), CPEC.gov.pk, provincial forest/wildlife
departments, and the Pakistan Bureau of Statistics.

## The Indus Waters Treaty dispute section

That section deliberately reports **positions and claims made by named parties** (Pakistan, India,
the Court of Arbitration, the Neutral Expert process) with sources, rather than presenting either
side's claims as settled fact — this is a live, unresolved bilateral dispute. Update the timeline
and sources in `geopolitics.py` as the process develops.

## Indus Delta Climate Impact Study page

The **🌴 Indus Delta Climate Impact Study** page loads real findings from Siyal, A.A. & Hashmi, Z.R.,
*"Impact of Climate Change in the Indus River Delta and Coastal Region of Pakistan"* (Final Project
Report, funded by GCISC, Islamabad), including the study's actual EC/pH/ESP soil-salinity statistics,
the 1990-2019 land-use/salinity time series (Table 3.2 of the report), Kotri Barrage flow history and
the 2004 IPOE environmental-flow recommendation, sea-level-rise/LECZ exposure figures, and the
report's economic-loss estimates and recommendations. These are that study's findings, reproduced
as data (not the original report text) — cite the original report if republishing this material.

## Extending this project

This is a strong working core, not an exhaustive encyclopedia. Natural next additions:
- Populate `coordinates.py` and `data_loader.py` with GPS-verified points and additional forests/
  parks/lakes not yet listed.
- Add OCR (pytesseract + pdf2image, requires poppler) for scanned/image-only PDFs — the extraction
  pathway in `file_analytics.py` already flags when a PDF has no extractable text/tables.
- Wire in live telemetry feeds (WAPDA/IRSA APIs, if available) in place of the uploaded-CSV workflow.
- Add a proper EMI/soil-salinity interpolation module (kriging/IDW) for Indus Delta EC/pH/ESP/
  soil-salinity mapping if you have field sample data.
