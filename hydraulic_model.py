"""
hydraulic_model.py
Lightweight scenario / risk-index engine and a simple telemetry-variance
analysis utility. These are transparent, editable heuristic models meant
for exploratory scenario comparison - NOT a calibrated hydrological model.
"""
import numpy as np
import pandas as pd


def compute_risk_index(exposure, vulnerability, sensitivity, adaptive_capacity, criticality):
    """
    All inputs on a 0-10 scale.
    Risk Index = (Exposure * Vulnerability * Sensitivity * Criticality) / (1 + Adaptive_Capacity)
    normalized to 0-100. Adaptive capacity reduces the realized risk.
    This is a heuristic composite index for scenario comparison, not a
    validated disaster-risk model.
    """
    raw = (exposure * vulnerability * sensitivity * criticality) / (1 + adaptive_capacity)
    max_raw = (10 * 10 * 10 * 10) / 1.0
    return round(100 * raw / max_raw, 2)


def scenario_table(exposure, vulnerability, sensitivity, adaptive_capacity, criticality):
    """Builds Baseline / Medium / Worst-Case rows by scaling inputs."""
    scenarios = {
        "Baseline": dict(e=exposure * 0.6, v=vulnerability * 0.6, s=sensitivity * 0.6,
                         a=min(10, adaptive_capacity * 1.2), c=criticality * 0.6),
        "Medium": dict(e=exposure, v=vulnerability, s=sensitivity, a=adaptive_capacity, c=criticality),
        "Worst-Case": dict(e=min(10, exposure * 1.4), v=min(10, vulnerability * 1.4),
                           s=min(10, sensitivity * 1.4), a=max(0, adaptive_capacity * 0.6),
                           c=min(10, criticality * 1.4)),
    }
    rows = []
    for label, p in scenarios.items():
        idx = compute_risk_index(p["e"], p["v"], p["s"], p["a"], p["c"])
        rows.append({"Scenario": label, "Exposure": round(p["e"], 1), "Vulnerability": round(p["v"], 1),
                     "Sensitivity": round(p["s"], 1), "Adaptive Capacity": round(p["a"], 1),
                     "Asset Criticality": round(p["c"], 1), "Risk Index (0-100)": idx})
    return pd.DataFrame(rows)


def simulate_glof_hydrograph(peak_discharge_cumecs=800, base_flow_cumecs=50, duration_hours=48, peak_hour=6):
    """
    Simple synthetic GLOF-style hydrograph simulation (gamma-shaped rise/fall)
    for illustrating a downstream flood pulse. Not a calibrated model -
    for scenario/education purposes only.
    """
    hours = np.arange(0, duration_hours, 0.5)
    shape = 2.2
    scale = peak_hour / shape
    # Gamma-shaped rise/fall curve computed directly (no scipy dependency):
    curve = (hours ** shape) * np.exp(-hours / max(scale, 0.1))
    curve = curve / curve.max()
    discharge = base_flow_cumecs + curve * (peak_discharge_cumecs - base_flow_cumecs)
    return pd.DataFrame({"hour": hours, "discharge_cumecs": discharge})


def river_basin_telemetry_variance(df, basin_col, value_col):
    """
    Given an uploaded telemetry dataframe with a basin/station identifier
    column and a numeric reading column (e.g. discharge, EC, pH, DO),
    returns basins ranked by variance (highest first) - answers:
    'which river basin reports the highest average telemetry data variance?'
    """
    if basin_col not in df.columns or value_col not in df.columns:
        return None
    grp = df.groupby(basin_col)[value_col].agg(["mean", "var", "std", "count"]).reset_index()
    grp = grp.sort_values("var", ascending=False)
    grp = grp.rename(columns={"mean": f"{value_col}_mean", "var": f"{value_col}_variance",
                               "std": f"{value_col}_std", "count": "n_readings"})
    return grp


WATER_QUALITY_INDEXES = {
    "EC": "Electrical Conductivity (dS/m or µS/cm) - proxy for total dissolved salts; central to soil/water salinity assessment (e.g. Indus Delta EMI surveys).",
    "pH": "Acidity/alkalinity of soil or water; affects nutrient availability and crop suitability.",
    "ESP": "Exchangeable Sodium Percentage - indicates sodicity hazard in irrigated/delta soils.",
    "DO": "Dissolved Oxygen (mg/L) - key indicator of aquatic ecosystem health, especially relevant to aquaculture zones and the Indus Delta/mangrove system.",
    "Soil Salinity": "Often assessed via EMI (Electromagnetic Induction) surveys and soil sampling, interpolated across a delta/command area to map salinization risk.",
}
