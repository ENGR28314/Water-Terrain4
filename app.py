"""
app.py
Pakistan Water, Terrain & Risk Dashboard
Creator: Engr. Syed Hassan Iqbal Shah

Run with:  streamlit run app.py
"""
import streamlit as st
import pandas as pd
import plotly.express as px

import data_loader as dl
import coordinates as coords
import map_view as mv
import network_view as nv
import hydraulic_model as hm
import file_analytics as fa
import geopolitics as geo
import sdg_module as sdg
import indus_delta as delta
import telemetry_network as telem
import indus_delta as ind

st.set_page_config(page_title=dl.APP_TITLE, layout="wide", page_icon="🌊")

# ---------------------------------------------------------------------------
# SIDEBAR: navigation, province filter, global search
# ---------------------------------------------------------------------------
st.sidebar.title("🌊 Pakistan Water & Terrain")
st.sidebar.caption(f"Creator: {dl.CREATOR_NAME}")

PAGES = [
    "🏠 Overview",
    "🗺️ Provinces & Territories",
    "🏞️ Rivers & Confluences",
    "🚧 Dams, Barrages & Link Canals",
    "📡 WAPDA Flood-Forecasting Telemetry Network",
    "💧 Lakes & Deserts",
    "🌴 Indus Delta Climate Impact Study",
    "🌡️ Climate Regions",
    "⛰️ Mountain Ranges & Peaks",
    "🌲 Forests",
    "🏕️ National Parks",
    "⚠️ Disaster Risk Profile",
    "🧮 Risk Scenario Engine",
    "📊 Socio-Economic Domain",
    "🌾 Agro-Economic Domain",
    "🏗️ Geo-Political & Strategic (CPEC / Hydropower)",
    "⚖️ Indus Waters Treaty Dispute",
    "🌴 Indus Delta Climate Impact Study",
    "🌍 ESG / ISO / SDG / MDG / Vision 2030",
    "📁 File Analytics & Data-Driven Maps",
    "🔍 Global Search",
    "📚 References",
]
page = st.sidebar.radio("Navigate", PAGES, index=0)

st.sidebar.markdown("---")
province_filter = st.sidebar.selectbox("Province / Region filter (applies where relevant)",
                                        ["All"] + list(dl.PROVINCES.keys()))
search_query = st.sidebar.text_input("Global search", placeholder="e.g. Tarbela, Chenab, Kirthar...")
st.sidebar.markdown("---")
st.sidebar.caption("Data is representative/educational. Validate against WAPDA, IRSA, PMD and provincial departments before operational use.")

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------
def filtered_regional_df():
    df = pd.DataFrame(dl.REGIONAL_AGRO_SOCIO_DATA)
    if province_filter != "All":
        short = province_filter.split(" (")[0]
        df = df[df["province"].str.contains(short.split()[0], case=False, na=False)]
    return df


def chart_controls(df, key_prefix):
    c1, c2, c3, c4 = st.columns(4)
    chart_type = c1.selectbox("Graph type", ["Bar chart", "Pie chart", "Scatter plot", "Line chart"], key=f"{key_prefix}_type")
    metric_label = c2.selectbox("Metric", list(dl.METRIC_OPTIONS.keys()), key=f"{key_prefix}_metric")
    x_col = c3.selectbox("X axis", df.columns.tolist(), index=0, key=f"{key_prefix}_x")
    color_col = c4.selectbox("Color / group by (optional)", ["(none)"] + df.columns.tolist(), key=f"{key_prefix}_color")
    y_col = dl.METRIC_OPTIONS[metric_label]
    color_col = None if color_col == "(none)" else color_col
    return chart_type, x_col, y_col, color_col


# ---------------------------------------------------------------------------
# PAGE: OVERVIEW
# ---------------------------------------------------------------------------
if page == "🏠 Overview":
    st.title(dl.APP_TITLE)
    st.caption(f"Created by {dl.CREATOR_NAME}")
    st.write(
        "An integrated reference dashboard for Pakistan's water systems, terrain, disaster-risk "
        "context, socio-economic & agro-economic indicators, and the strategic/geo-political "
        "dimensions of Indus basin water management."
    )
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Provinces / Territories", len(dl.PROVINCES))
    c2.metric("Major Rivers Tracked", len(dl.RIVERS))
    c3.metric("Dams Tracked", len(dl.DAMS))
    c4.metric("National Parks Tracked", len(dl.NATIONAL_PARKS))
    st.info(
        "Use the sidebar to navigate sections, filter by province/region, or run a global search. "
        "The **File Analytics** page lets you upload your own CSV / XLSX / PDF data and generate "
        "charts and maps from it directly."
    )
    st.subheader("Module Map")
    st.markdown(
        "- **Water & Terrain**: provinces, rivers, dams/barrages/canals, lakes, deserts, climate, mountains, forests, parks\n"
        "- **Disaster Risk**: hazard profile, exposure/vulnerability, scenario engine\n"
        "- **Socio-Economic & Agro-Economic**: food security, employment, IBIS, Rabi/Kharif, apiculture, aquaculture\n"
        "- **Strategic**: CPEC/hydropower, inter-provincial disputes, Indus Waters Treaty dispute (reported positions)\n"
        "- **Sustainability frameworks**: ESG / ISO / SDG / MDG / Vision 2030\n"
        "- **File Analytics**: upload your own CSV/XLSX/PDF for charts, cleaned-data export, and maps"
    )

# ---------------------------------------------------------------------------
# PAGE: PROVINCES
# ---------------------------------------------------------------------------
elif page == "🗺️ Provinces & Territories":
    st.title("Provinces & Territories of Pakistan")
    provs = dl.PROVINCES if province_filter == "All" else {province_filter: dl.PROVINCES[province_filter]}
    for name, info in provs.items():
        with st.expander(f"{name} — capital: {info['capital']} ({info['type']})", expanded=(len(provs) == 1)):
            st.write(f"**Major rivers:** {', '.join(info['major_rivers'])}")
            st.write(f"**Climate regions:** {', '.join(info['climate_regions'])}")
            st.write(info["notes"])

# ---------------------------------------------------------------------------
# PAGE: RIVERS
# ---------------------------------------------------------------------------
elif page == "🏞️ Rivers & Confluences":
    st.title("Rivers, Upstream/Downstream & Confluences")
    tab1, tab2 = st.tabs(["Details", "Network Diagram"])
    with tab1:
        for river, info in dl.RIVERS.items():
            with st.expander(river):
                st.write(f"**Source:** {info['source']}")
                st.write(f"**Path:** {info['path']}")
                st.write(f"**Upstream reach:** {info['upstream']}")
                st.write(f"**Downstream reach:** {info['downstream']}")
                st.write(f"**Confluences:** {', '.join(info['confluences'])}")
                st.write(f"**Basin classification:** {info['basin']}")
    with tab2:
        fig = nv.build_river_network_figure(dl.RIVERS)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Blue nodes = rivers; orange nodes = confluence points.")

# ---------------------------------------------------------------------------
# PAGE: DAMS / BARRAGES / LINK CANALS
# ---------------------------------------------------------------------------
elif page == "🚧 Dams, Barrages & Link Canals":
    st.title("Dams, Barrages / Headworks & Link Canals")
    tab1, tab2, tab3, tab4 = st.tabs(["Dams", "Barrages / Headworks", "Link Canals", "Map"])
    with tab1:
        st.dataframe(pd.DataFrame(dl.DAMS), use_container_width=True)
    with tab2:
        st.dataframe(pd.DataFrame(dl.BARRAGES), use_container_width=True)
    with tab3:
        st.dataframe(pd.DataFrame(dl.LINK_CANALS), use_container_width=True)
        fig = nv.build_canal_link_figure(dl.LINK_CANALS)
        st.plotly_chart(fig, use_container_width=True)
    with tab4:
        pts = []
        for d in dl.DAMS:
            if d["name"] in coords.DAM_COORDINATES:
                lat, lon = coords.DAM_COORDINATES[d["name"]]
                pts.append({"name": d["name"], "lat": lat, "lon": lon, "notes": d["purpose"]})
        for b in dl.BARRAGES:
            if b["name"] in coords.BARRAGE_COORDINATES:
                lat, lon = coords.BARRAGE_COORDINATES[b["name"]]
                pts.append({"name": b["name"], "lat": lat, "lon": lon, "notes": b["note"]})
        m = mv.build_point_map(pts, color="darkblue")
        st.components.v1.html(m._repr_html_(), height=520)

# ---------------------------------------------------------------------------
# PAGE: WAPDA TELEMETRY NETWORK (from uploaded WAPDA slides + IWT map)
# ---------------------------------------------------------------------------
elif page == "📡 WAPDA Flood-Forecasting Telemetry Network":
    st.title("WAPDA Flood-Forecasting Telemetry & Communications Network")
    st.caption(telem.SOURCE_NOTE)
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Meteorburst System", "HF Radio — Western Rivers", "Wireless Network — Eastern Rivers",
        "Station Map", "IWT Reference Map (Barrages & Canals)",
    ])

    with tab1:
        mb = telem.METEORBURST_SYSTEM
        st.subheader(mb["name"])
        st.write(f"**Master Station:** {mb['legend']['Master Station']}")
        c1, c2 = st.columns(2)
        c1.write("**Rain Sites**")
        for s in mb["legend"]["Rain Sites"]:
            c1.markdown(f"- {s}")
        c2.write("**River & Rain Sites**")
        for s in mb["legend"]["River & Rain Sites"]:
            c2.markdown(f"- {s}")
        st.write("**Other reference points on the source map:** " + ", ".join(mb["other_reference_points_on_map"]))
        st.write("**Rivers covered:** " + ", ".join(mb["rivers_covered"]))
        st.caption(mb["note"])

    with tab2:
        hf = telem.HF_RADIO_WESTERN_RIVERS
        st.subheader(hf["name"])
        for g in hf["groups"]:
            with st.expander(f"Hub: {g['hub']}"):
                if g["stations"]:
                    for s in g["stations"]:
                        st.markdown(f"- {s}")
                else:
                    st.write("(Reports directly to the Water Resource Management Directorate)")
        st.info(hf["flow"])

    with tab3:
        wl = telem.WIRELESS_EASTERN_RIVERS
        st.subheader(wl["name"])
        for g in wl["groups"]:
            with st.expander(f"River: {g['river']}"):
                for s in g["stations"]:
                    st.markdown(f"- {s}")

    with tab4:
        pts = []
        for name, latlon in coords.TELEMETRY_STATION_COORDINATES.items():
            pts.append({"name": name, "lat": latlon[0], "lon": latlon[1], "notes": "WAPDA telemetry/communications station"})
        m = mv.build_point_map(pts, color="darkgreen", zoom=6)
        st.components.v1.html(m._repr_html_(), height=560)
        st.caption("Station coordinates are approximate (town/site-level), for reference orientation only — not surveyed GPS points.")

    with tab5:
        st.subheader("Indus Waters Treaty — Link Canals & Barrages (reference map)")
        st.caption(telem.IWT_MAP_SOURCE_NOTE)
        c1, c2 = st.columns(2)
        c1.write("**Link canals shown on the map:**")
        for lc in telem.IWT_MAP_LINK_CANALS:
            c1.markdown(f"- {lc}")
        c2.write("**Barrages/headworks shown on the map:**")
        for b in telem.IWT_MAP_BARRAGES:
            c2.markdown(f"- {b}")
        st.write("**Additional rivers shown:** " + ", ".join(telem.IWT_MAP_ADDITIONAL_RIVERS))
        st.write("**Coastal feature noted:** " + telem.IWT_MAP_FEATURES["coastal_features"][0])
        st.caption(telem.IWT_MAP_FEATURES["boundary_notes"])

# ---------------------------------------------------------------------------
# PAGE: LAKES & DESERTS
# ---------------------------------------------------------------------------
elif page == "💧 Lakes & Deserts":
    st.title("Lakes & Deserts")
    tab1, tab2, tab3 = st.tabs(["Lakes", "Deserts", "Lakes Map"])
    with tab1:
        st.dataframe(pd.DataFrame(dl.LAKES), use_container_width=True)
    with tab2:
        st.dataframe(pd.DataFrame(dl.DESERTS), use_container_width=True)
    with tab3:
        pts = [{"name": l["name"], "lat": coords.LAKE_COORDINATES[l["name"]][0],
                "lon": coords.LAKE_COORDINATES[l["name"]][1], "notes": l["type"]}
               for l in dl.LAKES if l["name"] in coords.LAKE_COORDINATES]
        m = mv.build_point_map(pts, color="cadetblue")
        st.components.v1.html(m._repr_html_(), height=520)

# ---------------------------------------------------------------------------
# PAGE: INDUS DELTA CLIMATE IMPACT STUDY (MUET / GCISC report)
# ---------------------------------------------------------------------------
elif page == "🌴 Indus Delta Climate Impact Study":
    st.title("Indus River Delta: Climate Change Impact Study")
    st.caption(ind.REPORT_CITATION)
    tabs = st.tabs([
        "Location & Climate", "Soil Salinity (EC/pH/ESP)", "Salt-Affected Land Over Time",
        "Kotri Barrage Flow", "Sea-Level Rise & Coastal Risk", "Economic Loss", "Recommendations", "Map",
    ])
    with tabs[0]:
        st.write(ind.LOCATION["description"])
        c1, c2, c3 = st.columns(3)
        c1.metric("Delineated delta area", f"{ind.LOCATION['delineated_area_sq_km']:,} sq. km")
        c2.metric("Mean annual rainfall", f"{ind.CLIMATE['mean_annual_rainfall_mm']} mm")
        c3.metric("Mean temperature", f"{ind.CLIMATE['mean_temperature_c']} °C")
        st.write(ind.LOCATION["ramsar_status"])
        st.write(ind.LOCATION["delineated_area_note"])
        with st.expander("Other published delta-area estimates (for comparison)"):
            st.dataframe(pd.DataFrame(ind.DELTA_AREA_ESTIMATES), use_container_width=True)

    with tabs[1]:
        st.write(f"**Sampling:** {ind.SOIL_SAMPLING_METHOD['samples']} soil samples from "
                 f"{ind.SOIL_SAMPLING_METHOD['locations']} locations, at depths "
                 f"{', '.join(ind.SOIL_SAMPLING_METHOD['depths_cm'])} cm, validated with an EMI "
                 f"(EM38-MK2) survey — {ind.SOIL_SAMPLING_METHOD['note']}")
        st.dataframe(pd.DataFrame(ind.EC_PH_ESP_BY_DEPTH), use_container_width=True)
        st.write(f"**Overall finding:** {ind.SALINITY_FINDINGS['pattern']}")
        st.info(f"An estimated {ind.SALINITY_FINDINGS['pct_delta_salt_affected']} of the delta is "
                f"salt-affected. {ind.SALINITY_FINDINGS['temporal_change']}")
        st.subheader("Soil texture (0-60 cm profile)")
        tex = ind.SOIL_TEXTURE_SUMMARY
        tex_df = pd.DataFrame({
            "Class": ["Silty clay + clay loam", "Loam", "Clay", "Silty clay loam", "Other (silt loam, sandy, etc.)"],
            "Percent": [tex["silty_clay_and_clay_loam_pct"], tex["loam_pct"], tex["clay_pct"],
                        tex["silty_clay_loam_pct"], tex["other_pct"]],
        })
        fig = px.pie(tex_df, names="Class", values="Percent", title="Soil texture distribution")
        st.plotly_chart(fig, use_container_width=True)

    with tabs[2]:
        df = pd.DataFrame(ind.LANDUSE_TIMESERIES)
        st.dataframe(df, use_container_width=True)
        pct_df = df.melt(id_vars="year", value_vars=["water_pct", "normal_pct", "salt_affected_pct", "makli_hills_pct"],
                          var_name="class", value_name="percent")
        fig = px.line(pct_df, x="year", y="percent", color="class", markers=True,
                      title="Indus Delta land-use classification over time (% of delta)")
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Source: classified Landsat imagery, 1990-2019 (Table 3.2 of the source report).")

    with tabs[3]:
        kb = ind.KOTRI_BARRAGE_FLOW
        c1, c2 = st.columns(2)
        c1.metric("Pre-dam avg. annual discharge", f"{kb['pre_dam_avg_annual_discharge_BCM']} BCM")
        c2.metric("Pre-dam avg. annual sediment", f"{kb['pre_dam_avg_annual_sediment_million_tons']} million tons")
        st.write(kb["decline_driver"])
        st.write(kb["zero_flow_history"])
        ipoe = kb["ipoe_2004_recommendation"]
        st.warning(f"IPOE (2004) recommended a continuous flow of {ipoe['continuous_flow_cusecs']:,} cusecs "
                   f"year-round below Kotri, plus {ipoe['five_year_flood_flow_MAF']} MAF over five years as "
                   f"flood flows. {ipoe['note']}")
        rel = kb["flow_salinity_relationship"]
        st.write(f"**Flow vs. salinity relationship:** {rel['interpretation']}")
        st.caption(f"R² (salt-affected area vs. flow) = {rel['salt_affected_area_vs_flow_R2']}; "
                   f"R² (normal-soil area vs. flow) = {rel['normal_soil_area_vs_flow_R2']}")

    with tabs[4]:
        slr = ind.SEA_LEVEL_AND_COASTAL_RISK
        st.write(slr["global_context"])
        st.write(slr["delta_topography"])
        c1, c2, c3 = st.columns(3)
        c1.metric("Delta in LECZ (<10 m)", f"{slr['lecz_area_pct']}%")
        c2.metric("Area below 1 m elevation", f"{slr['area_below_1m_pct']}%")
        c3.metric("Area below 5 m elevation", f"{slr['area_below_5m_pct']}%")
        st.write(slr["note"])

    with tabs[5]:
        el = ind.ECONOMIC_LOSS_ESTIMATES
        c1, c2 = st.columns(2)
        c1.metric("Est. annual degradation cost", f"US$ {el['annual_degradation_cost_usd_billion']} billion")
        c2.metric("Cultivable delta area", f"{el['cultivable_area_ha']:,} ha ({el['cultivable_area_pct_of_delta']}%)")
        st.write(el["degradation_cost_source"])
        st.write(el["loss_composition_note"])
        c1, c2 = st.columns(2)
        c1.metric("Illustrative Kharif flood loss", f"Rs. {el['kharif_flood_loss_estimate_pkr_billion']} billion")
        c2.metric("Illustrative Rabi flood loss", f"Rs. {el['rabi_flood_loss_estimate_pkr_billion']} billion")
        st.caption(el["assumptions"])

    with tabs[6]:
        st.subheader("Study Recommendations")
        for r in ind.RECOMMENDATIONS:
            st.markdown(f"- {r}")
        st.subheader("Key Conclusions")
        for c in ind.CONCLUSIONS_SUMMARY:
            st.markdown(f"- {c}")

    with tabs[7]:
        pts = [{"name": t, "lat": v[0], "lon": v[1]} for t, v in coords.INDUS_DELTA_TOWN_COORDINATES.items()]
        m = mv.build_point_map(pts, center=(24.4, 68.0), zoom=9, color="darkgreen")
        st.components.v1.html(m._repr_html_(), height=500)
        st.caption("Delta towns referenced in the source study (approximate locations).")

# ---------------------------------------------------------------------------
# PAGE: CLIMATE REGIONS
# ---------------------------------------------------------------------------
elif page == "🌡️ Climate Regions":
    st.title("Climatic Regions of Pakistan")
    for region, desc in dl.CLIMATE_REGIONS.items():
        st.subheader(region)
        st.write(desc)

# ---------------------------------------------------------------------------
# PAGE: MOUNTAIN RANGES
# ---------------------------------------------------------------------------
elif page == "⛰️ Mountain Ranges & Peaks":
    st.title("Mountain Ranges of Pakistan")
    for group, ranges in dl.MOUNTAIN_RANGES.items():
        st.header(group)
        for rname, info in ranges.items():
            with st.expander(rname):
                st.write(f"**Highest peak:** {info['highest_peak']}")
                st.write(f"**Location:** {info['location']}")
                st.write(f"**Rivers flowing through / from this range:** {', '.join(info['rivers'])}")
                st.write(f"**Geology:** {info['geology']}")
                st.write(f"**Tourist / climbing notes:** {info['tourism']}")
    st.subheader("Peaks Map")
    pts = [{"name": k, "lat": v[0], "lon": v[1]} for k, v in coords.MOUNTAIN_PEAK_COORDINATES.items()]
    m = mv.build_point_map(pts, color="darkred", zoom=5)
    st.components.v1.html(m._repr_html_(), height=520)

# ---------------------------------------------------------------------------
# PAGE: FORESTS
# ---------------------------------------------------------------------------
elif page == "🌲 Forests":
    st.title("Forests of Pakistan")
    st.subheader("Main Forest Types")
    for ftype, desc in dl.FOREST_TYPES.items():
        st.markdown(f"**{ftype}** — {desc}")
    st.markdown("---")
    st.subheader("Notable Forests — Details")
    names = [f["name"] for f in dl.NOTABLE_FORESTS]
    sel = st.selectbox("Select a forest for details", names)
    forest = next(f for f in dl.NOTABLE_FORESTS if f["name"] == sel)
    c1, c2 = st.columns(2)
    c1.write(f"**Type:** {forest['type']}")
    c1.write(f"**Location:** {forest['location']}")
    c1.write(f"**Covered area:** {forest['area']}")
    c2.write(f"**History & origin:** {forest['history']}")
    c2.write(f"**Wildlife & nature:** {forest['wildlife']}")
    c2.write(f"**Attractions & recreation:** {forest['attractions']}")

# ---------------------------------------------------------------------------
# PAGE: NATIONAL PARKS
# ---------------------------------------------------------------------------
elif page == "🏕️ National Parks":
    st.title("National Parks of Pakistan")
    tab1, tab2 = st.tabs(["All Parks Map", "Select a park for details"])
    with tab1:
        pts = [{"name": p, "lat": coords.PARK_COORDINATES[p][0], "lon": coords.PARK_COORDINATES[p][1]}
               for p in dl.NATIONAL_PARKS if p in coords.PARK_COORDINATES]
        m = mv.build_point_map(pts, color="green", zoom=5)
        st.components.v1.html(m._repr_html_(), height=520)
    with tab2:
        sel = st.selectbox("Select a park for details", dl.NATIONAL_PARKS)
        if sel in coords.PARK_COORDINATES:
            lat, lon = coords.PARK_COORDINATES[sel]
            st.write(f"**Coordinates (approx.):** {lat}, {lon}")
            m2 = mv.build_single_park_map(sel, lat, lon)
            st.components.v1.html(m2._repr_html_(), height=450)
        else:
            st.warning("Coordinates not yet catalogued for this park — add them in coordinates.py (PARK_COORDINATES).")

# ---------------------------------------------------------------------------
# PAGE: DISASTER RISK PROFILE
# ---------------------------------------------------------------------------
elif page == "⚠️ Disaster Risk Profile":
    st.title("National Disaster Risk Context")
    st.header("1. Hazard Profile")
    for cat, items in dl.HAZARD_PROFILE.items():
        with st.expander(cat):
            for it in items:
                st.markdown(f"- {it}")
    st.header("2. Exposure & Vulnerability Assessment")
    for k, v in dl.EXPOSURE_VULNERABILITY.items():
        st.subheader(k)
        if isinstance(v, list):
            for item in v:
                st.markdown(f"- {item}")
        else:
            st.write(v)
    st.header("3. Emerging Risks & Climate Change Trends")
    for k, v in dl.EMERGING_RISK_TRENDS.items():
        st.subheader(k)
        st.write(v)
    st.header("4. Risk Scenarios")
    for k, v in dl.RISK_SCENARIOS.items():
        st.markdown(f"**{k}:** {v}")

# ---------------------------------------------------------------------------
# PAGE: RISK SCENARIO ENGINE
# ---------------------------------------------------------------------------
elif page == "🧮 Risk Scenario Engine":
    st.title("Engineering / Scenario Module")
    st.caption("Heuristic composite index for scenario comparison — not a calibrated hydrological or engineering model.")
    c1, c2, c3, c4, c5 = st.columns(5)
    exposure = c1.slider("Exposure", 0, 10, 6)
    vulnerability = c2.slider("Population Vulnerability", 0, 10, 5)
    sensitivity = c3.slider("Sensitivity", 0, 10, 5)
    adaptive_capacity = c4.slider("Adaptive Capacity", 0, 10, 4)
    criticality = c5.slider("Asset/Service Criticality", 0, 10, 6)

    idx = hm.compute_risk_index(exposure, vulnerability, sensitivity, adaptive_capacity, criticality)
    st.metric("Current Risk Index (0-100)", idx)

    df_scenarios = hm.scenario_table(exposure, vulnerability, sensitivity, adaptive_capacity, criticality)
    st.dataframe(df_scenarios, use_container_width=True)
    fig = px.bar(df_scenarios, x="Scenario", y="Risk Index (0-100)", color="Scenario",
                 title="Baseline / Medium / Worst-Case Risk Index")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Simulation Engine: Synthetic GLOF-style Hydrograph")
    c1, c2, c3 = st.columns(3)
    peak_q = c1.number_input("Peak discharge (cumecs)", 50, 5000, 800)
    base_q = c2.number_input("Base flow (cumecs)", 0, 500, 50)
    peak_hr = c3.number_input("Time to peak (hours)", 1, 24, 6)
    hydro_df = hm.simulate_glof_hydrograph(peak_q, base_q, 48, peak_hr)
    fig2 = px.line(hydro_df, x="hour", y="discharge_cumecs", title="Synthetic Downstream Flood Pulse (illustrative)")
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("Illustrative synthetic curve for scenario communication only — not derived from a calibrated basin model.")

# ---------------------------------------------------------------------------
# PAGE: SOCIO-ECONOMIC
# ---------------------------------------------------------------------------
elif page == "📊 Socio-Economic Domain":
    st.title("Socio-Economic Domain")
    st.markdown(
        "**Covers:** Food Security · Employment · Urban Growth · Tourism · Domestic & Industrial "
        "Utility · Climate & Vulnerability · Energy Generation"
    )
    st.subheader("Input-Driven Regional Socio-Economic Data (editable)")
    df = filtered_regional_df().reset_index(drop=True)
    edited = st.data_editor(df, use_container_width=True, num_rows="dynamic", key="socio_editor")
    chart_type, x_col, y_col, color_col = chart_controls(edited, "socio")
    if x_col and y_col in edited.columns:
        fig = fa.make_chart(edited, chart_type, x_col=x_col, y_col=y_col, color_col=color_col,
                             title=f"{y_col} by {x_col}")
        st.plotly_chart(fig, use_container_width=True)
    st.download_button("Download this data as CSV", fa.to_csv_bytes(edited), "socio_economic_data.csv", "text/csv")

# ---------------------------------------------------------------------------
# PAGE: AGRO-ECONOMIC
# ---------------------------------------------------------------------------
elif page == "🌾 Agro-Economic Domain":
    st.title("Agro-Economic Domain")
    st.markdown("**World's Largest Contiguous Irrigation System:** the Indus Basin Irrigation System (IBIS).")
    tab1, tab2, tab3, tab4 = st.tabs(["Rabi Season", "Kharif Season", "Apiculture & Aquaculture", "Input-Driven Data & Graphs"])
    with tab1:
        st.dataframe(pd.DataFrame(dl.RABI_CROPS), use_container_width=True)
    with tab2:
        st.dataframe(pd.DataFrame(dl.KHARIF_CROPS), use_container_width=True)
    with tab3:
        st.write("**Apiculture indicators**")
        st.dataframe(pd.DataFrame(dl.APICULTURE), use_container_width=True)
        st.write("**Aquaculture indicators**")
        st.dataframe(pd.DataFrame(dl.AQUACULTURE), use_container_width=True)
    with tab4:
        df = filtered_regional_df().reset_index(drop=True)
        edited = st.data_editor(df, use_container_width=True, num_rows="dynamic", key="agro_editor")
        chart_type, x_col, y_col, color_col = chart_controls(edited, "agro")
        if x_col and y_col in edited.columns:
            fig = fa.make_chart(edited, chart_type, x_col=x_col, y_col=y_col, color_col=color_col,
                                 title=f"{y_col} by {x_col}")
            st.plotly_chart(fig, use_container_width=True)
        st.download_button("Download this data as CSV", fa.to_csv_bytes(edited), "agro_economic_data.csv", "text/csv")

# ---------------------------------------------------------------------------
# PAGE: GEO-POLITICAL / STRATEGIC (CPEC etc.)
# ---------------------------------------------------------------------------
elif page == "🏗️ Geo-Political & Strategic (CPEC / Hydropower)":
    st.title("Geo-Political & Strategic Domain")
    tab1, tab2, tab3 = st.tabs(["CPEC Hydropower Portfolio", "Diamer-Bhasha Dam", "Inter-Provincial (Punjab vs Sindh)"])
    with tab1:
        df = pd.DataFrame(dl.CPEC_HYDROPOWER)
        st.dataframe(df, use_container_width=True)
        fig = px.bar(df, x="name", y="capacity_mw", color="status", title="CPEC Hydropower Capacity (MW)")
        st.plotly_chart(fig, use_container_width=True)
        st.caption("China is a dominant source of FDI in Pakistan's hydropower asset portfolio via these CPEC-linked projects.")
    with tab2:
        d = dl.DIAMER_BHASHA
        st.metric("Planned capacity", f"{d['capacity_mw']} MW")
        st.write(f"**Storage:** {d['storage']}")
        st.write(f"**Status note:** {d['status_note']}")
        for s in d["sources"]:
            st.markdown(f"- {s}")
    with tab3:
        st.subheader("Sindh's position (as reported)")
        st.write(dl.PUNJAB_SINDH_DISPUTE["sindh_position"])
        st.subheader("Punjab's position (as reported)")
        st.write(dl.PUNJAB_SINDH_DISPUTE["punjab_position"])
        st.subheader("Structural gridlock")
        st.write(dl.PUNJAB_SINDH_DISPUTE["structural_gridlock"])
        st.subheader("Legal / institutional mechanisms")
        st.write(f"**IRSA:** {dl.IRSA_CCI_MECHANISMS['IRSA']}")
        st.write(f"**CCI:** {dl.IRSA_CCI_MECHANISMS['CCI']}")
        st.write(f"**Supreme Court review:** {dl.IRSA_CCI_MECHANISMS['Supreme Court']}")
        st.write(dl.IRSA_CCI_MECHANISMS["notes"])

# ---------------------------------------------------------------------------
# PAGE: INDUS WATERS TREATY DISPUTE  (neutral framing — reported positions)
# ---------------------------------------------------------------------------
elif page == "⚖️ Indus Waters Treaty Dispute":
    st.title("Indus Waters Treaty (IWT): Indian Upstream Projects Dispute")
    st.caption(
        "This section summarizes a live, contested bilateral dispute. Content is presented as "
        "reported positions/claims made by Pakistan, India, and treaty bodies, with sources — "
        "not as adjudicated fact."
    )
    tabs = st.tabs([
        "IWT Overview", "Timeline", "Pakistan's Position", "India's Position",
        "Pakal Dul & Ratle — Technical Points", "Neutral Expert Timeline",
        "Head Marala / Crop-Impact Issue", "CoA (PCA) Timeline & Validity", "India's Proposed Canal Projects",
    ])
    with tabs[0]:
        st.write(geo.IWT_OVERVIEW)
    with tabs[1]:
        st.dataframe(pd.DataFrame(geo.TIMELINE_2025_2026), use_container_width=True)
    with tabs[2]:
        st.write(geo.PAKISTAN_POSITION)
    with tabs[3]:
        st.write(geo.INDIA_POSITION)
    with tabs[4]:
        st.write("Technical points Pakistan has raised in IWT proceedings regarding **Pakal Dul (1,000 MW)** and **Ratle (850 MW)** (and the related Kishanganga precedent):")
        st.dataframe(pd.DataFrame(geo.TECHNICAL_DISPUTE_POINTS), use_container_width=True)
    with tabs[5]:
        st.write("World Bank-appointed Neutral Expert (Michel Lino) published technical review calendar:")
        st.dataframe(pd.DataFrame(geo.NEUTRAL_EXPERT_TIMELINE), use_container_width=True)
    with tabs[6]:
        st.warning(geo.HEAD_MARALA_ISSUE)
    with tabs[7]:
        st.write(geo.COA_VALIDITY_NOTE)
        st.write("**31 Aug 2026 interim order:** " + geo.TIMELINE_2025_2026[-1]["event"])
    with tabs[8]:
        st.write(geo.INDIA_PROPOSED_CANAL_PROJECTS)

    st.markdown("---")
    st.subheader("Sources for this section")
    for s in geo.GEOPOLITICAL_SOURCES:
        st.markdown(f"- [{s['label']}]({s['url']})")

# ---------------------------------------------------------------------------
# PAGE: INDUS DELTA CLIMATE IMPACT STUDY (from uploaded MUET/GCISC report)
# ---------------------------------------------------------------------------
elif page == "🌴 Indus Delta Climate Impact Study":
    st.title(delta.REPORT_META["title"])
    st.caption(f"{delta.REPORT_META['authors']} — funded by {delta.REPORT_META['funder']} ({delta.REPORT_META['pages']} pp.)")
    st.write(delta.DELTA_OVERVIEW)

    tabs = st.tabs([
        "Location & Delineation", "Soil Texture & Salinity (EC/pH/ESP)", "Kotri Barrage Flow History",
        "Sea-Level Rise Context", "Coastal Elevation & LECZ", "Economic Loss Estimates", "Recommendations",
    ])

    with tabs[0]:
        loc = delta.DELTA_LOCATION
        st.write(f"**Extent:** {loc['extent']}")
        st.write(f"**Climate:** {loc['climate']}")
        st.info(loc["area_estimates_note"])
        st.write("Delta area estimates cited across the reviewed literature:")
        st.dataframe(pd.DataFrame(delta.DELTA_AREA_LITERATURE), use_container_width=True)
        fig = px.bar(pd.DataFrame(delta.DELTA_AREA_LITERATURE), x="reference", y="sq_km",
                     title="Cited Indus Delta area estimates by source (sq. km)")
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

    with tabs[1]:
        st.subheader("Soil Texture (0-60 cm profile)")
        tex = delta.SOIL_TEXTURE
        tex_df = pd.DataFrame({
            "Class": ["Silty clay & clay loam", "Loam", "Clay", "Silty clay loam", "Other (silt loam, sandy clay loam, sandy loam, sand)"],
            "Share (%)": [tex["silty_clay_and_clay_loam_pct"], tex["loam_pct"], tex["clay_pct"],
                          tex["silty_clay_loam_pct"], tex["other_pct"]],
        })
        c1, c2 = st.columns([1, 1])
        c1.dataframe(tex_df, use_container_width=True)
        fig = px.pie(tex_df, names="Class", values="Share (%)", title="Soil texture composition")
        c2.plotly_chart(fig, use_container_width=True)
        st.caption(tex["note"])

        st.subheader("Salinity Findings (EC, pH, ESP, Soil Salinity)")
        sal = delta.SALINITY_FINDINGS
        st.write(f"**EC (Electrical Conductivity):** {sal['EC_note']}")
        st.write(f"**pH:** {sal['pH_note']}")
        st.metric("Delta soil reported as salt-affected", f"{sal['salt_affected_pct_of_delta']}%+")
        c1, c2 = st.columns(2)
        c1.metric("Irrigated salt-affected land (change over ~3 decades)",
                   f"{sal['irrigated_salt_affected_change']['from_pct']}% → {sal['irrigated_salt_affected_change']['to_pct']}%")
        c2.metric("Normal (non-saline) soil area (change over ~3 decades)",
                   f"{sal['normal_soil_change']['from_pct']}% → {sal['normal_soil_change']['to_pct']}%")
        st.write(f"Kotri flow vs. salt-affected area: R² = {sal['kotri_flow_vs_salt_affected_area_R2']} (negative/weak). "
                 f"Kotri flow vs. normal soil area: R² = {sal['kotri_flow_vs_normal_soil_area_R2']} (positive/weak).")
        st.write(sal["interpretation"])
        with st.expander("Water quality / soil indexes reference (EC, pH, ESP, DO)"):
            for k, v in hm.WATER_QUALITY_INDEXES.items():
                st.markdown(f"- **{k}:** {v}")

    with tabs[2]:
        kf = delta.KOTRI_FLOW_HISTORY
        c1, c2 = st.columns(2)
        c1.metric("Pre-dam avg. annual discharge below Kotri", f"{kf['pre_dam_avg_annual_discharge_BCM']} BCM")
        c2.metric("Pre-dam avg. annual sediment load", f"{kf['pre_dam_avg_annual_sediment_million_tons']} million tons")
        st.write(f"**Zero-flow onset:** {kf['zero_flow_onset']}")
        st.write(f"**Zero-flow peak period:** {kf['zero_flow_peak']}")
        st.write(f"**Current status:** {kf['current_status']}")
        st.info(f"**IPOE (2004) environmental-flow recommendation:** {kf['environmental_flow_recommendation']}")

    with tabs[3]:
        slr = delta.SEA_LEVEL_RISE_CONTEXT
        st.write(f"**Historical rate:** {slr['historical_rate']}")
        st.write("**Projections cited in the study:**")
        for p in slr["projections_cited"]:
            st.markdown(f"- {p}")

    with tabs[4]:
        lecz = delta.COASTAL_ELEVATION_LECZ
        c1, c2, c3 = st.columns(3)
        c1.metric("Delta area < 1 m elevation", f"{lecz['lt_1m_sq_km']:,} sq. km ({lecz['lt_1m_pct_of_delta']}%)")
        c2.metric("Delta area < 5 m elevation", f"{lecz['lt_5m_sq_km']:,} sq. km ({lecz['lt_5m_pct_of_delta']}%)")
        c3.metric("Delta area in LECZ (<10 m)", f"{lecz['lecz_lt_10m_sq_km']:,} sq. km ({lecz['lecz_pct_of_delta']}%)")
        st.caption(lecz["note"])
        elev_df = pd.DataFrame({
            "Elevation band": ["0-1 m", "1-3 m", "3-5 m", "5-10 m", "10-20 m", "20-60 m"],
            "Approx. share": [22.5, 15, 31.5, 24, 5, 2],  # illustrative split summing toward reported <1m/<5m/LECZ bands
        })
        st.caption("Illustrative elevation-band distribution consistent with the <1 m / <5 m / LECZ cumulative figures reported above (exact per-band figures were not tabulated in the source text).")
        fig = px.bar(elev_df, x="Elevation band", y="Approx. share", title="Indus Delta area by elevation band (illustrative)")
        st.plotly_chart(fig, use_container_width=True)

    with tabs[5]:
        econ = delta.ECONOMIC_LOSS_ESTIMATES
        st.metric("Estimated annual economic cost of delta degradation", f"US$ {econ['annual_degradation_cost_usd_billion']} billion")
        st.caption(econ["cost_source"])
        c1, c2, c3 = st.columns(3)
        c1.metric("Cultivable agricultural land", f"{econ['cultivable_agri_land_ha']:,} ha")
        c2.metric("Actually cultivated (Rabi+Kharif)", f"{econ['actually_cultivated_ha']:,} ha")
        c3.metric("Flood-vulnerable cultivated land (in LECZ)", f"{econ['flood_vulnerable_acres_93pct_LECZ']:,} acres")
        loss_df = pd.DataFrame({
            "Season": ["Kharif", "Rabi"],
            "Estimated agricultural loss (PKR billion)": [econ["kharif_flood_loss_estimate_pkr_billion"], econ["rabi_flood_loss_estimate_pkr_billion"]],
        })
        fig = px.bar(loss_df, x="Season", y="Estimated agricultural loss (PKR billion)",
                     title="Estimated agricultural loss from coastal flooding, by season")
        st.plotly_chart(fig, use_container_width=True)
        st.caption(econ["loss_calc_assumptions"])

    with tabs[6]:
        for r in delta.RECOMMENDATIONS:
            st.markdown(f"- {r}")

    st.markdown("---")
    st.caption(delta.SOURCE_CITATION)

# ---------------------------------------------------------------------------
# PAGE: ESG / ISO / SDG / MDG / VISION 2030
# ---------------------------------------------------------------------------
elif page == "🌍 ESG / ISO / SDG / MDG / Vision 2030":
    st.title("Sustainability & Governance Frameworks")
    st.subheader("UN Sustainable Development Goals (SDG) — Linkages")
    st.dataframe(pd.DataFrame(sdg.SDG_TARGETS), use_container_width=True)
    st.subheader("MDG Legacy")
    st.write(sdg.MDG_LEGACY_NOTE)
    st.subheader("Vision 2030 (Pakistan)")
    st.write(sdg.VISION_2030_NOTE)
    st.subheader("ISO & ESG Frameworks")
    st.dataframe(pd.DataFrame(sdg.ISO_ESG_FRAMEWORKS), use_container_width=True)

# ---------------------------------------------------------------------------
# PAGE: FILE ANALYTICS
# ---------------------------------------------------------------------------
elif page == "📁 File Analytics & Data-Driven Maps":
    st.title("File Analytics: Upload Your Own Data")
    st.write("Upload CSV, XLSX/XLS, or PDF files. Numeric columns are auto-detected for charting; "
             "lat/lon-style columns are auto-detected for mapping.")

    uploaded = st.file_uploader("Upload file(s)", type=["csv", "xlsx", "xls", "pdf"], accept_multiple_files=True)

    combined_df = None
    if uploaded:
        for f in uploaded:
            st.markdown(f"### {f.name}")
            if f.name.lower().endswith(".pdf"):
                result = fa.extract_pdf_content(f)
                st.info(result["message"])
                if result["text"]:
                    with st.expander("Extracted text (preview)"):
                        st.text(result["text"][:3000])
                for i, tbl in enumerate(result["tables"]):
                    st.write(f"Table {i+1} extracted from PDF:")
                    st.dataframe(tbl, use_container_width=True)
                    combined_df = tbl
            else:
                df, msg = fa.load_tabular_file(f)
                st.info(msg)
                if df is not None:
                    df = fa.clean_dataframe(df)
                    st.dataframe(df.head(50), use_container_width=True)
                    combined_df = df
                    st.download_button(f"Download cleaned CSV ({f.name})", fa.to_csv_bytes(df),
                                        f"cleaned_{f.name.rsplit('.',1)[0]}.csv", "text/csv", key=f"dl_{f.name}")

    st.markdown("---")
    st.subheader("Chart Builder")
    if combined_df is not None and len(combined_df.columns) >= 1:
        numeric_cols = fa.detect_numeric_columns(combined_df)
        all_cols = combined_df.columns.tolist()
        c1, c2, c3, c4 = st.columns(4)
        chart_type = c1.selectbox("Graph type", ["Bar chart", "Pie chart", "Scatter plot", "Line chart"], key="fa_type")
        x_col = c2.selectbox("X axis", all_cols, key="fa_x")
        y_col = c3.selectbox("Y axis (numeric)", numeric_cols if numeric_cols else all_cols, key="fa_y")
        color_col = c4.selectbox("Color / group (optional)", ["(none)"] + all_cols, key="fa_color")
        color_col = None if color_col == "(none)" else color_col
        try:
            fig = fa.make_chart(combined_df, chart_type, x_col=x_col, y_col=y_col, color_col=color_col,
                                 title=f"{y_col} by {x_col}")
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Could not build chart with the selected columns: {e}")
    else:
        st.caption("Upload a CSV/XLSX file (or a PDF with an extractable table) above to build a chart.")

    st.markdown("---")
    st.subheader("Map From Uploaded Data")
    st.caption("If your uploaded file has latitude/longitude-style columns, plot them on a map.")
    if combined_df is not None:
        norm = mv.dataframe_from_upload_points(combined_df)
        if norm is not None and len(norm) > 0:
            m = mv.build_point_map(norm, color="purple")
            st.components.v1.html(m._repr_html_(), height=520)
        else:
            st.info("No latitude/longitude columns detected in the uploaded data.")

    st.markdown("---")
    st.subheader("River Basin Telemetry Variance & Water Quality Indexes")
    st.write("Analyze which river basin/station reports the highest telemetry variance for a chosen "
             "indicator (e.g. discharge, EC, pH, ESP, or dissolved oxygen — DO).")
    with st.expander("Water quality index reference"):
        for k, v in hm.WATER_QUALITY_INDEXES.items():
            st.markdown(f"- **{k}:** {v}")
    if combined_df is not None:
        c1, c2 = st.columns(2)
        basin_col = c1.selectbox("Basin / station column", combined_df.columns.tolist(), key="basin_col")
        value_col = c2.selectbox("Telemetry value column (numeric)",
                                  fa.detect_numeric_columns(combined_df) or combined_df.columns.tolist(), key="value_col")
        variance_df = hm.river_basin_telemetry_variance(combined_df, basin_col, value_col)
        if variance_df is not None:
            st.dataframe(variance_df, use_container_width=True)
            fig = px.bar(variance_df, x=basin_col, y=f"{value_col}_variance",
                         title=f"Variance of {value_col} by {basin_col} (highest first)")
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.caption("Upload telemetry CSV data above (with a basin/station column and a numeric reading column) to run this analysis.")

# ---------------------------------------------------------------------------
# PAGE: GLOBAL SEARCH
# ---------------------------------------------------------------------------
elif page == "🔍 Global Search":
    st.title("Global Search")
    q = search_query.strip().lower()
    if not q:
        st.info("Type a search term in the sidebar (e.g. a river, dam, forest, or park name).")
    else:
        results = []
        for r, info in dl.RIVERS.items():
            if q in r.lower():
                results.append(("River", r, info["path"]))
        for d in dl.DAMS:
            if q in d["name"].lower():
                results.append(("Dam", d["name"], d["purpose"]))
        for b in dl.BARRAGES:
            if q in b["name"].lower():
                results.append(("Barrage", b["name"], b["note"]))
        for l in dl.LAKES:
            if q in l["name"].lower():
                results.append(("Lake", l["name"], l["type"]))
        for f in dl.NOTABLE_FORESTS:
            if q in f["name"].lower():
                results.append(("Forest", f["name"], f["location"]))
        for p in dl.NATIONAL_PARKS:
            if q in p.lower():
                results.append(("National Park", p, ""))
        for prov, info in dl.PROVINCES.items():
            if q in prov.lower():
                results.append(("Province/Territory", prov, info["notes"]))
        if q in "indus delta" or q in "kotri" or q in "mangrove" or q in "salinity" or q in "sea level rise":
            results.append(("Study", "Indus Delta Climate Impact Study", delta.REPORT_META["title"]))
        if q in "telemetry" or q in "meteorburst" or q in "hf radio" or q in "badoki" or q in "wapda":
            results.append(("Network", "WAPDA Flood-Forecasting Telemetry Network", "Meteorburst system, HF Radio (Western Rivers), Wireless Network (Eastern Rivers)"))

        if results:
            st.dataframe(pd.DataFrame(results, columns=["Type", "Name", "Detail"]), use_container_width=True)
        else:
            st.warning("No matches found in the catalogued reference data.")

# ---------------------------------------------------------------------------
# PAGE: REFERENCES
# ---------------------------------------------------------------------------
elif page == "📚 References":
    st.title("References")
    for r in dl.REFERENCES:
        st.markdown(f"- [{r['label']}]({r['url']})")
    st.markdown("---")
    st.subheader("Indus Waters Treaty Dispute — additional sources")
    for s in geo.GEOPOLITICAL_SOURCES:
        st.markdown(f"- [{s['label']}]({s['url']})")
    st.markdown("---")
    st.subheader("Indus Delta Climate Impact Study — source")
    st.write(delta.SOURCE_CITATION)
    st.markdown("---")
    st.subheader("WAPDA Telemetry Network & Indus Waters Treaty Map — sources")
    st.write(telem.SOURCE_NOTE)
    st.write(telem.IWT_MAP_SOURCE_NOTE)

st.sidebar.markdown("---")
st.sidebar.caption(f"© {dl.CREATOR_NAME} — Pakistan Water & Terrain Dashboard")
