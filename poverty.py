"""
poverty.py
Pakistan's official 2024-25 poverty estimates, drawn from the user-uploaded
"Preliminary Report on Poverty Estimation 2024-25" (February 2026),
Government of Pakistan, Ministry of Planning, Development & Special
Initiatives, Economic Policy Wing (SDGs Section) / Uraan Pakistan.
"""

REPORT_META = {
    "title": "Preliminary Report on Poverty Estimation 2024-25",
    "publisher": "Government of Pakistan, Ministry of Planning, Development & Special Initiatives "
                 "(Economic Policy Wing, Sustainable Development Goals Section) - Uraan Pakistan",
    "date": "February 2026",
    "data_source": "Household Integrated Economic Survey (HIES) 2024-25 microdata (Pakistan Bureau of Statistics)",
}

METHODOLOGY = {
    "approach": "Cost of Basic Needs (CBN) - the official methodology since the 2013-14 poverty estimates, "
                "replacing the earlier Food Energy Intake (FEI) approach used from 1998-99.",
    "poverty_line_definition": "Minimum monthly expenditure per adult equivalent required to meet essential "
                                "food and non-food needs.",
    "poverty_line_2013_14": "Rs. 3,030 per adult equivalent per month (updated over time via CPI inflation adjustment).",
    "poverty_line_2024_25": "Rs. 8,484 per adult equivalent per month (CPI-adjusted).",
    "consumption_aggregate_components": ["Aggregate Nominal Consumption Expenditure (food + non-food, standardized monthly)",
                                          "Spatial Price Index (adjusts for regional cost-of-living differences)",
                                          "Equivalence Scale (adjusts for household size/age composition: 0.8 weight per person under 18, 1.0 for 18+)"],
    "governance": "A Technical Working Group was constituted 2 July 2025 (under the Chief Economist) for "
                  "preparatory work; a Poverty Estimation Committee (academia, federal/provincial governments, "
                  "research organizations, development partners) was notified 7 November 2025 and endorsed the "
                  "final estimates in meetings held January-February 2026.",
}

HEADLINE_RESULTS = {
    "poverty_line_2024_25_pkr_per_adult_equiv_month": 8484,
    "national_poverty_headcount_2024_25_pct": 28.9,
    "national_poverty_headcount_2018_19_pct": 21.9,
    "note": "Both figures use a consistent poverty-line benchmark; national poverty is reported to have "
            "risen from 21.9% (2018-19, the last HIES-based estimate) to 28.9% (2024-25).",
}

INCOME_CONSUMPTION_TREND = [
    {"year": "2015-16", "monthly_income_nominal_pkr": 35662, "monthly_income_real_pkr": 35662,
     "monthly_consumption_nominal_pkr": 32578, "monthly_consumption_real_pkr": 32578},
    {"year": "2018-19", "monthly_income_nominal_pkr": 41545, "monthly_income_real_pkr": 35454,
     "monthly_consumption_nominal_pkr": 37159, "monthly_consumption_real_pkr": 31711},
    {"year": "2024-25", "monthly_income_nominal_pkr": 82179, "monthly_income_real_pkr": 31127,
     "monthly_consumption_nominal_pkr": 79150, "monthly_consumption_real_pkr": 29980},
]
INCOME_CONSUMPTION_NOTE = ("Real income/consumption (base year 2015-16) declined even as nominal "
                            "figures rose sharply - i.e. inflation outpaced nominal household income growth.")

MACRO_DETERMINANTS = {
    "gdp_inflation_series": [
        {"year": "2015-16", "real_gdp_growth_pct": 4.1, "cpi_inflation_pct": 4.9},
        {"year": "2016-17", "real_gdp_growth_pct": 4.9, "cpi_inflation_pct": 4.8},
        {"year": "2017-18", "real_gdp_growth_pct": 6.1, "cpi_inflation_pct": 5.1},
        {"year": "2018-19", "real_gdp_growth_pct": 3.1, "cpi_inflation_pct": 6.8},
        {"year": "2019-20", "real_gdp_growth_pct": -0.9, "cpi_inflation_pct": 10.7},
        {"year": "2020-21", "real_gdp_growth_pct": 5.7, "cpi_inflation_pct": 8.9},
        {"year": "2021-22", "real_gdp_growth_pct": 6.2, "cpi_inflation_pct": 12.2},
        {"year": "2022-23", "real_gdp_growth_pct": -0.2, "cpi_inflation_pct": 29.2},
        {"year": "2023-24", "real_gdp_growth_pct": 2.5, "cpi_inflation_pct": 23.4},
        {"year": "2024-25", "real_gdp_growth_pct": 3.1, "cpi_inflation_pct": 4.5},
    ],
    "shocks": ["COVID-19 pandemic (sharp economic contraction, 2019-20)",
               "Global commodity super-cycle -> multi-decade-high domestic inflation (peak 29.2% in 2022-23)",
               "Geopolitical disruptions to supply chains",
               "2022 floods: estimated losses of US$30.1 billion",
               "2025 floods: estimated losses of US$2.9 billion"],
    "lag_note": "Macroeconomic stability (stronger growth, moderating inflation, fiscal consolidation, rising "
                "remittances) improved from FY2025 into H1 FY2025-26, but real wage recovery, employment "
                "expansion and household balance-sheet restoration have not yet caught up - so early "
                "stabilization can coexist with rising measured poverty.",
    "remittances_note": "Remittances rose but had limited poverty-reducing impact - unevenly distributed, "
                         "mainly benefiting households already linked to migration networks; functioned more "
                         "as a shock-coping mechanism than a broad-based income driver.",
}

SOCIAL_DETERMINANTS = {
    "Security challenges": "Disrupt livelihoods and access to markets/services, disproportionately raising poverty in Khyber Pakhtunkhwa and Balochistan.",
    "Human capital constraints": "Limited access to quality education/skills forces many into low-wage work over skill investment, perpetuating low productivity across generations.",
    "Regional & structural disparities": "Challenging terrain and rural areas face infrastructure/connectivity/market-access disadvantages; low labor mobility reinforces persistent regional poverty patterns.",
    "Social protection (BISP)": "During FY2025, Rs. 592.4 billion was disbursed under the Benazir Income Support Programme (BISP) - a 27.1% increase year-on-year - reaching approximately 10 million beneficiaries by 30 June 2025. The report notes cumulative economic/climate shocks have exceeded what social transfers alone can offset.",
}

CONCLUSION_NOTE = (
    "Poverty rose in 2024-25 versus 2018-19, reflecting the cumulative impact of COVID-19, the global "
    "commodity super-cycle's inflationary pressure, geopolitical supply-chain disruption, and severe flood "
    "shocks (2022 and 2025). The report frames continued poverty reduction as depending on sustained "
    "employment growth, real income recovery, and strengthened social-protection coverage, alongside the "
    "macroeconomic stabilization already under way."
)

SOURCE_NOTE = (
    "Source: 'Preliminary Report on Poverty Estimation 2024-25' (February 2026), Government of Pakistan, "
    "Ministry of Planning, Development & Special Initiatives, Economic Policy Wing (SDGs Section) / "
    "Uraan Pakistan. Uploaded by the user."
)
