"""
indus_delta.py
Data drawn from: Siyal, A.A. & Hashmi, Z.R. (2019), "Impact of Climate Change
in the Indus River Delta and Coastal Region of Pakistan", funded by the
Global Change Impact Studies Centre (GCISC), Islamabad.
Source PDF uploaded by the user (MUET technical study).

All figures below are as reported in that study; treat them as that
study's findings, not independently re-verified by this dashboard.
"""

REPORT_META = {
    "title": "Impact of Climate Change in the Indus River Delta and Coastal Region of Pakistan",
    "authors": "Dr. Altaf Ali Siyal, Dr. Zia ur Rehman Hashmi",
    "funder": "Global Change Impact Studies Centre (GCISC), Islamabad",
    "pages": 53,
}

DELTA_OVERVIEW = """
The Indus Delta is reported as the world's 5th largest delta, stretching from Sir Creek in the
east to Phitti Creek in the west, with its apex near Banoo town, Sujawal district, Sindh. It is a
Ramsar wetland site and reportedly supports the 7th largest mangrove ecosystem in the world,
with about 97% of Pakistan's total mangrove forest concentrated in the delta (~95% of it
Avicennia marina). The delta is reported to provide livelihoods to roughly 0.9 million coastal
residents, and — due to its flat, high-energy coastline — is described as receiving more wave
energy per day than the Mississippi Delta receives in a year.
"""

DELTA_LOCATION = {
    "extent": "Longitude 67°11'9.76\" E to 68°44'46.23\" E; Latitude 23°47'25.20\" N to 24°57'30.90\" N",
    "climate": "Arid, mean annual rainfall < 200 mm; average temperatures 23.8-28.7 °C; ~80% of rainfall falls during the June-September monsoon.",
    "area_estimates_note": "Cited delta-area estimates vary widely across the literature reviewed by the study (from 5,000 to 41,440 sq. km depending on the source/delineation method used) — the study notes this made delineating a single study boundary difficult.",
}

DELTA_AREA_LITERATURE = [
    {"sq_km": 6000, "hectares": 600000, "reference": "Meynell & Qureshi (1993); Khan & Akbar (2012); Giri et al. (2015); Memon (2005)"},
    {"sq_km": 8500, "hectares": 850000, "reference": "Ahmed & Shaukat (2015)"},
    {"sq_km": 30000, "hectares": 3000000, "reference": "Leichenko et al. (1993); Renaud et al. (2013)"},
    {"sq_km": 17000, "hectares": 1700000, "reference": "Syvitski et al. (2013)"},
    {"sq_km": 16000, "hectares": 1600000, "reference": "Callaghan (2014)"},
    {"sq_km": 41440, "hectares": 4144000, "reference": "Peracha et al. (2015)"},
    {"sq_km": 5000, "hectares": 500000, "reference": "Laghari et al. (2015)"},
]

SOIL_TEXTURE = {
    "silty_clay_and_clay_loam_pct": 48,
    "loam_pct": 16,
    "clay_pct": 15,
    "silty_clay_loam_pct": 10,
    "other_pct": 11,  # silt loam, sandy clay loam, sandy loam, sand
    "note": "Reported for the 0-60 cm soil profile; the delta is dominated by heavy, fine-textured soils.",
}

SALINITY_FINDINGS = {
    "EC_note": "Vast areas along the southern coastal belt have EC (electrical conductivity of soil saturation extract) greater than 15 dS/m, attributed to subsurface seawater intrusion; EC decreases significantly further from the sea and increases with decreasing soil depth.",
    "pH_note": "Most sampled soils had pH within 8.5; soils from/near tidal floodplains showed higher pH, attributed to higher sodium content.",
    "salt_affected_pct_of_delta": 80,  # "more than 80%"
    "irrigated_salt_affected_change": {"period": "last ~3 decades", "from_pct": 57.4, "to_pct": 57.7},
    "normal_soil_change": {"period": "same ~3 decades", "from_pct": 29.3, "to_pct": 26.7},
    "kotri_flow_vs_salt_affected_area_R2": 0.483,  # negative/weak relationship
    "kotri_flow_vs_normal_soil_area_R2": 0.370,    # positive/weak relationship
    "interpretation": "More flow below Kotri Barrage is weakly associated with more normal (less saline) soil area and less salt-affected area — i.e. reduced downstream freshwater flow is associated with increasing soil salinization, though the relationship is statistically weak.",
}

KOTRI_FLOW_HISTORY = {
    "pre_dam_avg_annual_discharge_BCM": 107,
    "pre_dam_avg_annual_sediment_million_tons": 193,
    "zero_flow_onset": "No zero-flow days recorded before 1962. Zero-flow days began after the Kotri and Guddu Barrages were commissioned (1962-1967).",
    "zero_flow_peak": "Zero/no-flow days rose to as many as 250 days per year in the post-Kotri/post-Mangla period (1967-1975).",
    "current_status": "Downstream Kotri Barrage flow is now largely constrained to two monsoon months (August-September).",
    "environmental_flow_recommendation": "International Panel of Experts (IPOE, 2004) recommended a minimum 5,000 cusecs flow year-round below Kotri, plus 25 MAF released over 5 years (~5 MAF/year) as Kharif flood flows, to limit seawater intrusion and meet ecological needs.",
}

SEA_LEVEL_RISE_CONTEXT = {
    "historical_rate": "~0.6 mm/year in the late 19th century, rising to ~1.8 mm/year by the mid-20th century, and ~3 mm/year in the first decade of the 21st century (as cited in the study); 20th-century global average sea level rose an estimated 17 cm.",
    "projections_cited": [
        "IPCC (2007): +21 to +71 cm by 2070 (best estimate ~44 cm).",
        "IPCC (Meehl et al., 2007): +0.18 to 0.59 m by end of 21st century.",
        "Horton et al. (2008): +0.62 to 0.88 m by 2100.",
        "Rohling et al. (2008), paleoclimatic evidence: a rate of up to 1.6 m/century considered possible.",
    ],
}

COASTAL_ELEVATION_LECZ = {
    "lt_1m_sq_km": 29400, "lt_1m_pct_of_delta": 22.5,
    "lt_5m_sq_km": 90410, "lt_5m_pct_of_delta": 69,
    "lecz_lt_10m_sq_km": 12248, "lecz_pct_of_delta": 93.7,
    "note": "Nearly all major delta towns sit within the Low-Elevation Coastal Zone (LECZ, <10 m elevation), placing them at high risk of coastal flood inundation.",
}

ECONOMIC_LOSS_ESTIMATES = {
    "annual_degradation_cost_usd_billion": 2.0,
    "cost_source": "World Bank (2019), as cited in the study; roughly half attributed to agricultural loss (waterlogging/salinity) and half to ecosystem degradation (mangroves, fisheries) per Sanchez-Triana et al. (2015).",
    "cultivable_agri_land_ha": 313608,   # ~24% of delta
    "actually_cultivated_ha": 219500,    # ~70% of cultivable, Rabi+Kharif
    "actually_cultivated_acres": 542450,
    "flood_vulnerable_acres_93pct_LECZ": 504450,
    "kharif_flood_loss_estimate_pkr_billion": 30,
    "rabi_flood_loss_estimate_pkr_billion": 27,
    "loss_calc_assumptions": "Based on an assumed average rice yield of 60 maunds/acre at Rs. 1,000/maund; excludes environmental, ecological and infrastructure losses, which the study notes would also be severe.",
}

RECOMMENDATIONS = [
    "Introduce and encourage biosaline agriculture (e.g. Pal grass, Quinoa, Salicornia, Sea Aster, Spartina alterniflora) on tidal floodplains and barren salt-affected land, especially on the left bank of the Indus, to support food/fodder security and poverty mitigation.",
    "Extend the existing 38 km coastal highway (right bank) a further ~180 km on the left bank, with a bridge over the Indus at Kharo Chhan — to improve market access, tourism, and act as a defense line against surface seawater intrusion, cyclones and tsunami risk.",
    "Ensure a minimum environmental flow of 5,000 cusecs year-round below Kotri Barrage, plus ~5 MAF/year of Kharif flood flow (IPOE 2004 recommendation), to limit seawater intrusion and sustain delta flora/fauna.",
    "Ensure sufficient canal water originating from Kotri Barrage (alongside river environmental flow) to reduce surface/subsurface seawater intrusion and supply drinking water to coastal communities.",
    "Restore old relic river channels (e.g. Ochito, Old Pinyari) to carry flood water to the sea, reduce levee-breach risk, and supply freshwater to remote coastal communities.",
    "Revitalize the delta's mostly-saline natural lakes with freshwater during monsoon season, supporting drinking water supply and groundwater recharge.",
    "Encourage tourism (e.g. mangrove-creek boat cruising) to improve local socio-economic conditions.",
]

SOURCE_CITATION = (
    "Siyal, A.A. & Hashmi, Z.R. (2019). Impact of Climate Change in the Indus River Delta and "
    "Coastal Region of Pakistan. Funded by the Global Change Impact Studies Centre (GCISC), "
    "Islamabad. (Study data: soil sampling + EMI survey with EM38-MK2; Kotri Barrage flow "
    "records 1937-38 to 2018 from Sindh Irrigation Department; Landsat imagery 1990-2018 via "
    "USGS GloVis; SRTM 30 m DEM via USGS EarthExplorer.)"
)

# Backward-compatible alias: some deployed copies of app.py reference this
# module as `ind` and call `ind.REPORT_CITATION` instead of SOURCE_CITATION.
REPORT_CITATION = SOURCE_CITATION
