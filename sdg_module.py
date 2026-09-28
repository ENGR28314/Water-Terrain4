"""
sdg_module.py
ESG / ISO / UN SDG / MDG / Vision 2030 reference mapping relevant to
water, food, and environmental themes covered by this dashboard.
"""

SDG_TARGETS = [
    {"sdg": "SDG 1", "title": "No Poverty", "linkage": "Socio-economic stratification & vulnerability module; poverty alleviation framing for disaster-risk exposure."},
    {"sdg": "SDG 2", "title": "Zero Hunger", "linkage": "Rabi/Kharif crop production, food-security indicator in the socio-economic domain."},
    {"sdg": "SDG 6", "title": "Clean Water and Sanitation", "linkage": "Dams/barrages/link canals module; water-quality indexes (EC, pH, ESP, DO)."},
    {"sdg": "SDG 7", "title": "Affordable and Clean Energy", "linkage": "Hydropower portfolio (Tarbela, Mangla, CPEC projects, Diamer-Bhasha)."},
    {"sdg": "SDG 8", "title": "Decent Work and Economic Growth", "linkage": "Employment metric in the regional agro-socio dataset."},
    {"sdg": "SDG 11", "title": "Sustainable Cities and Communities", "linkage": "Urban flooding hazard, urban growth indicator."},
    {"sdg": "SDG 13", "title": "Climate Action", "linkage": "GLOF risk, monsoon variability, glacier melt, sea-level rise modules."},
    {"sdg": "SDG 14", "title": "Life Below Water", "linkage": "Mangrove forests, coastal aquaculture, Indus Delta salinity/EMI survey data."},
    {"sdg": "SDG 15", "title": "Life on Land", "linkage": "Forest types, national parks, mountain-range biodiversity."},
    {"sdg": "SDG 16", "title": "Peace, Justice and Strong Institutions", "linkage": "IRSA/CCI dispute-resolution mechanisms; IWT/PCA arbitration module."},
    {"sdg": "SDG 17", "title": "Partnerships for the Goals", "linkage": "CPEC co-financed hydropower, World Bank-linked IWT appointing mechanisms."},
]

# ---------------------------------------------------------------------------
# OFFICIAL NATIONAL SDG FRAMEWORK (Government of Pakistan, Planning Commission,
# Ministry of Planning, Development & Reform, March 2018) - "Summary for the
# National Economic Council (NEC): Sustainable Development Goals (SDGs)
# National Framework". Baselines are 2014-15; targets are for 2030.
# ---------------------------------------------------------------------------
NATIONAL_SDG_FRAMEWORK_META = {
    "adopted_by_parliament": "February 2016",
    "internalized_in": "Pakistan Vision 2025 (signed Sep 2015)",
    "total_goals": 17, "total_targets": 169, "total_indicators": 230,
    "process": "Federal SDG Unit (Planning Commission) + provincial SDG Units; divisional-level negotiations "
               "in all 4 provinces; a national community-based survey; a 7-criterion multi-criteria prioritization "
               "model (width, depth, multiplier effect, urgency, low resource requirement, less structural "
               "change, relevance for all provinces).",
    "data_gap_note": "Of 230 indicators, reliable data was unavailable for at least one-fourth; another 45% "
                      "existed only in scattered, unanalyzed form.",
}

NATIONAL_SDG_PRIORITY_CATEGORIES = {
    "Category I (short-run, immediate policy intervention)": [
        "Food security through sustainable agriculture", "Improved nutrition and healthy life",
        "Equitable quality education", "Improved drinking water and hygiene facilities",
        "Affordable and clean energy", "Responsive institutions that ensure peace and security",
        "Access to affordable, reliable and sustainable energy for all",
    ],
    "Category II (longer timeframe, consistent policy support)": [
        "Accelerating the rate of poverty reduction through coordinated interventions",
        "Empowerment of women and girls through institutional strengthening",
        "Building resilient infrastructure and smart cities (urban and rural)",
    ],
    "Category III (long gestation, major institutional reform needed)": [
        "Mitigating the impact of climate change", "Conservation and sustainable use of marine resources",
    ],
}

NATIONAL_SDG_INDICATORS = [
    {"goal": "Goal 1: No Poverty", "target": "1.2 Halve poverty in all its dimensions (national definition)",
     "indicator": "Proportion of population below the national poverty line", "baseline_2014_15": "29.50%", "target_2030": "9.00%"},
    {"goal": "Goal 1: No Poverty", "target": "1.3 Social protection coverage of the poor/vulnerable",
     "indicator": "Proportion of population covered by social protection floors/systems", "baseline_2014_15": "29.90%", "target_2030": "70.00%"},
    {"goal": "Goal 2: Zero Hunger", "target": "2.1 End hunger, ensure access to safe/nutritious food",
     "indicator": "Prevalence of undernourishment", "baseline_2014_15": "20%", "target_2030": "5%"},
    {"goal": "Goal 2: Zero Hunger", "target": "2.2 End malnutrition (stunting/wasting) in children under 5",
     "indicator": "Stunting / Wasting / Underweight prevalence", "baseline_2014_15": "43.7% / 15.1% / 31.5%", "target_2030": "21.9% / 7.5% / 10.0%"},
    {"goal": "Goal 3: Good Health & Well-being", "target": "3.1 Reduce maternal mortality",
     "indicator": "Maternal mortality ratio (per 100,000 live births)", "baseline_2014_15": "276", "target_2030": "179"},
    {"goal": "Goal 3: Good Health & Well-being", "target": "3.2 End preventable child deaths",
     "indicator": "Under-five mortality rate / Neonatal mortality rate (per 1,000)", "baseline_2014_15": "89 / 55", "target_2030": "40 / 25"},
    {"goal": "Goal 4: Quality Education", "target": "4.1 Universal completion of primary/secondary education",
     "indicator": "Proportion achieving minimum reading/maths proficiency", "baseline_2014_15": "Total 57% (Girls 53%, Boys 60%)", "target_2030": "100%"},
    {"goal": "Goal 4: Quality Education", "target": "4.6 Youth/adult literacy and numeracy",
     "indicator": "Functional literacy rate (Total / Female / Male)", "baseline_2014_15": "60% / 49% / 70%", "target_2030": "80% / 69% / 90%"},
    {"goal": "Goal 5: Gender Equality", "target": "5.5 Women's participation in leadership/decision-making",
     "indicator": "Proportion of women in managerial positions / parliament", "baseline_2014_15": "Mgmt 1.5% / Parl. 19.7%", "target_2030": "Mgmt 5.0% / Parl. 30%"},
    {"goal": "Goal 5: Gender Equality", "target": "5.b Women's access to enabling technology",
     "indicator": "Proportion of women owning a mobile telephone", "baseline_2014_15": "69.87%", "target_2030": "85%"},
    {"goal": "Goal 6: Clean Water & Sanitation", "target": "6.1 Universal access to safe drinking water",
     "indicator": "Proportion of population using safely managed drinking water", "baseline_2014_15": "36.0%", "target_2030": "100%"},
    {"goal": "Goal 6: Clean Water & Sanitation", "target": "6.2 Universal access to sanitation & hygiene",
     "indicator": "Proportion using safely managed sanitation services", "baseline_2014_15": "73%", "target_2030": "100%"},
    {"goal": "Goal 7: Affordable & Clean Energy", "target": "7.1 Universal access to electricity",
     "indicator": "Proportion of population with access to electricity", "baseline_2014_15": "93.50%", "target_2030": "100%"},
    {"goal": "Goal 7: Affordable & Clean Energy", "target": "7.2 Increase renewable energy share",
     "indicator": "Renewable energy share of final energy consumption", "baseline_2014_15": "11%", "target_2030": "25%"},
    {"goal": "Goal 8: Decent Work & Economic Growth", "target": "8.1 Sustain per-capita GDP growth",
     "indicator": "Annual growth rate of real GDP per capita", "baseline_2014_15": "1.00%", "target_2030": "5.00%"},
    {"goal": "Goal 8: Decent Work & Economic Growth", "target": "8.5 Full/productive employment, equal pay",
     "indicator": "Unemployment rate (Total / Male / Female)", "baseline_2014_15": "5.9% / 4.9% / 8.9%", "target_2030": "3.5% / 2.5% / 4.5%"},
    {"goal": "Goal 9: Industry, Innovation & Infrastructure", "target": "9.2 Raise industry's share of GDP/employment",
     "indicator": "Manufacturing value added as % of GDP", "baseline_2014_15": "13.56%", "target_2030": "16.00%"},
    {"goal": "Goal 9: Industry, Innovation & Infrastructure", "target": "9.5 Enhance R&D",
     "indicator": "R&D expenditure as % of GDP", "baseline_2014_15": "0.2%", "target_2030": "2.0%"},
    {"goal": "Goal 10: Reduced Inequalities", "target": "10.2 Reduce proportion below 50% of median income",
     "indicator": "Proportion of people living below 50% of median income", "baseline_2014_15": "16.60%", "target_2030": "Decrease 40% from baseline"},
    {"goal": "Goal 11: Sustainable Cities & Communities", "target": "11.1 Reduce slum/informal-housing population",
     "indicator": "Proportion of urban population in slums/informal settlements", "baseline_2014_15": "45.50%", "target_2030": "22.00%"},
    {"goal": "Goal 12: Responsible Consumption & Production", "target": "12.1 National SCP action plan",
     "indicator": "Sustainable Consumption & Production (SCP) national action plan status", "baseline_2014_15": "National SCP Action Plan exists", "target_2030": "Sub-national SCP action plans; upgraded national plan"},
    {"goal": "Goal 13: Climate Action", "target": "13.1/13.2 DRR strategy & climate policy integration",
     "indicator": "National/local DRR strategies; national climate policy status", "baseline_2014_15": "Pakistan has DRR plans; National Climate Change Policy (2012)", "target_2030": "Effective implementation of DRR & climate policy at national/sub-national level"},
    {"goal": "Goal 14: Life Below Water", "target": "14.1/14.2 Reduce marine pollution, protect coastal ecosystems",
     "indicator": "Coastal eutrophication/plastic-debris index; ecosystem-based EEZ management", "baseline_2014_15": "Not yet measured", "target_2030": "Enhanced conservation & sustainable use of oceans via implementing law"},
    {"goal": "Goal 15: Life on Land", "target": "15.1 Conserve forests/inland freshwater ecosystems",
     "indicator": "Forest area as % of total land area", "baseline_2014_15": "5.70%", "target_2030": "12.00%"},
    {"goal": "Goal 16: Peace, Justice & Strong Institutions", "target": "16.1 Reduce violence",
     "indicator": "Intentional homicide rate (per 100,000) / victimization from violence (12-mo)", "baseline_2014_15": "7.8% / 32.2%", "target_2030": "3.0% / 16.0%"},
    {"goal": "Goal 17: Partnerships for the Goals", "target": "17.1 Strengthen domestic resource mobilization",
     "indicator": "Total government revenue as % of GDP (tax-to-GDP)", "baseline_2014_15": "11.0%", "target_2030": "18.0%"},
]

NATIONAL_SDG_SOURCE_NOTE = (
    "Source: Government of Pakistan, Ministry of Planning, Development & Reform, Planning Commission "
    "(March 2018). 'Summary for the National Economic Council (NEC): Sustainable Development Goals (SDGs) "
    "National Framework.' Uploaded by the user. Figures shown are National Baseline (2014-15) vs. National "
    "Target (2030) as tabled for NEC approval; several national targets are set below the global SDG targets "
    "in light of Pakistan's resource and institutional constraints, per the source document."
)

MDG_LEGACY_NOTE = (
    "The Millennium Development Goals (2000-2015), particularly MDG 1 (poverty/hunger) and "
    "MDG 7 (environmental sustainability, incl. access to safe drinking water), set baselines "
    "that several current SDG water/food/poverty targets build on for Pakistan."
)

VISION_2030_NOTE = (
    "Pakistan's long-term national planning frameworks (successive 'Vision' documents) have "
    "emphasised water security, food security, energy security and climate resilience as "
    "recurring strategic pillars; this dashboard treats 'Vision 2030' references as a policy "
    "aspiration marker rather than a single authoritative source document."
)

ISO_ESG_FRAMEWORKS = [
    {"framework": "ISO 14001", "domain": "Environmental Management Systems", "relevance": "Applicable to dam/hydropower project environmental management plans."},
    {"framework": "ISO 26000", "domain": "Social Responsibility", "relevance": "Applicable to resettlement/community-impact aspects of large water infrastructure."},
    {"framework": "ISO 31000", "domain": "Risk Management", "relevance": "Framework basis for the disaster-risk scenario module's structure (exposure/vulnerability/response)."},
    {"framework": "ESG - Environmental", "domain": "Environmental performance", "relevance": "Water-quality indexes, forest cover, mangrove restoration tracking."},
    {"framework": "ESG - Social", "domain": "Social performance", "relevance": "Vulnerable-settlement exposure, employment and livelihoods in agro-economic module."},
    {"framework": "ESG - Governance", "domain": "Governance performance", "relevance": "IRSA/CCI transparency, treaty-compliance and dispute-resolution mechanisms."},
]
