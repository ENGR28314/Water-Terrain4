"""
map_view.py
Folium map builders: static reference maps + user-data-driven maps
(from uploaded CSV/PDF-extracted lat/lon points).
"""
import folium
import pandas as pd


def build_point_map(points, center=(30.3753, 69.3451), zoom=5, color="blue", popup_field="name"):
    """
    points: list of dicts with at least 'name','lat','lon' (or a DataFrame with those columns)
    Returns a folium.Map object.
    """
    m = folium.Map(location=center, zoom_start=zoom, tiles="OpenStreetMap")

    if isinstance(points, pd.DataFrame):
        records = points.to_dict("records")
    else:
        records = points

    for p in records:
        try:
            lat = float(p.get("lat"))
            lon = float(p.get("lon"))
        except (TypeError, ValueError):
            continue
        label = str(p.get(popup_field, p.get("name", "Point")))
        extra = p.get("notes", "")
        folium.Marker(
            location=(lat, lon),
            popup=folium.Popup(f"<b>{label}</b><br>{extra}", max_width=300),
            tooltip=label,
            icon=folium.Icon(color=color, icon="info-sign"),
        ).add_to(m)
    return m


def build_single_park_map(name, lat, lon, zoom=11):
    m = folium.Map(location=(lat, lon), zoom_start=zoom, tiles="OpenStreetMap")
    folium.Marker(
        location=(lat, lon),
        popup=name,
        tooltip=name,
        icon=folium.Icon(color="green", icon="tree-conifer", prefix="glyphicon"),
    ).add_to(m)
    folium.Circle(radius=3000, location=(lat, lon), color="green", fill=True, fill_opacity=0.08).add_to(m)
    return m


def build_river_basin_map(rivers_dict, coords_lookup=None):
    """Simple overview map with markers approximating each named river's mouth/reference point."""
    m = folium.Map(location=(29.0, 68.5), zoom_start=5, tiles="OpenStreetMap")
    fallback_pts = {
        "Indus": (24.8, 67.4), "Jhelum": (30.97, 72.15), "Chenab": (32.68, 74.46),
        "Ravi": (30.7, 73.0), "Sutlej": (29.4, 71.0), "Kabul River": (33.9, 72.2),
        "Swat River": (34.2, 71.7), "Hunza River": (36.1, 74.6),
    }
    for river in rivers_dict:
        pt = fallback_pts.get(river, (30.0, 70.0))
        folium.Marker(location=pt, tooltip=river, popup=river,
                      icon=folium.Icon(color="cadetblue", icon="tint")).add_to(m)
    return m


def dataframe_from_upload_points(df, lat_col=None, lon_col=None, name_col=None):
    """
    Given an arbitrary uploaded DataFrame, try to auto-detect lat/lon/name
    columns if not explicitly provided. Returns a normalized DataFrame with
    columns: name, lat, lon, notes (best effort).
    """
    cols_lower = {c.lower(): c for c in df.columns}

    def find_col(candidates):
        for cand in candidates:
            for lc, orig in cols_lower.items():
                if cand in lc:
                    return orig
        return None

    lat_col = lat_col or find_col(["lat", "latitude"])
    lon_col = lon_col or find_col(["lon", "lng", "longitude"])
    name_col = name_col or find_col(["name", "site", "station", "location", "place"])

    if not lat_col or not lon_col:
        return None

    out = pd.DataFrame()
    out["name"] = df[name_col] if name_col else [f"Point {i+1}" for i in range(len(df))]
    out["lat"] = pd.to_numeric(df[lat_col], errors="coerce")
    out["lon"] = pd.to_numeric(df[lon_col], errors="coerce")
    out["notes"] = ""
    out = out.dropna(subset=["lat", "lon"])
    return out
