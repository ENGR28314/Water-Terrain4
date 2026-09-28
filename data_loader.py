"""
data_loader.py
Static reference datasets for the Pakistan Water & Terrain dashboard.
All data here is representative / educational and should be validated
against primary sources (WAPDA, IRSA, PMD, Pakistan Forest Institute,
provincial wildlife/forest departments) before use in decision-making.
"""

CREATOR_NAME = "Engr. Syed Hassan Iqbal Shah"
APP_TITLE = "Pakistan Water, Terrain & Risk Dashboard"

# ---------------------------------------------------------------------------
# PROVINCES / TERRITORIES
# ---------------------------------------------------------------------------
PROVINCES = {
    "Punjab": {
        "capital": "Lahore", "type": "Province",
        "major_rivers": ["Indus", "Jhelum", "Chenab", "Ravi", "Sutlej", "Beas (border reach)"],
        "climate_regions": ["Arid", "Semi-Arid", "Tropical"],
        "notes": "Core of the Indus Basin Irrigation System; largest irrigated agricultural base.",
    },
    "Sindh": {
        "capital": "Karachi", "type": "Province",
        "major_rivers": ["Indus"],
        "climate_regions": ["Arid", "Tropical (coastal)"],
        "notes": "Lower riparian province; Indus Delta, coastal belt, Thar Desert.",
    },
    "Khyber Pakhtunkhwa (KPK)": {
        "capital": "Peshawar", "type": "Province",
        "major_rivers": ["Indus", "Kabul", "Swat", "Chitral/Kunar", "Panjkora"],
        "climate_regions": ["Temperate", "Highland", "Arid (southern districts)"],
        "notes": "Mountainous north with coniferous forests; hill-torrent and flash-flood exposure.",
    },
    "Balochistan": {
        "capital": "Quetta", "type": "Province",
        "major_rivers": ["Hingol", "Zhob", "Bolan", "Porali", "Nari"],
        "climate_regions": ["Arid", "Highland"],
        "notes": "Largest land area, lowest population density, chronic water stress and drought exposure.",
    },
    "Gilgit-Baltistan (GB)": {
        "capital": "Gilgit", "type": "Territory",
        "major_rivers": ["Indus", "Gilgit", "Hunza", "Shigar", "Shyok"],
        "climate_regions": ["Highland", "Polar (high-altitude ice/permafrost zones)"],
        "notes": "Source region of the Indus; highest concentration of glaciers and GLOF risk outside the poles.",
    },
    "Azad Jammu and Kashmir (AJK)": {
        "capital": "Muzaffarabad", "type": "Territory",
        "major_rivers": ["Jhelum", "Neelum", "Poonch"],
        "climate_regions": ["Temperate", "Highland"],
        "notes": "Jhelum basin; seismically active (2005 earthquake epicentre region nearby).",
    },
    "Islamabad Capital Territory (ICT)": {
        "capital": "Islamabad", "type": "Federal Territory",
        "major_rivers": ["Soan (Swaan)"],
        "climate_regions": ["Subtropical Highland"],
        "notes": "Federal capital; Margalla Hills form its northern boundary.",
    },
}

# ---------------------------------------------------------------------------
# RIVERS: upstream/downstream + confluences
# ---------------------------------------------------------------------------
RIVERS = {
    "Indus": {
        "source": "Tibetan Plateau (near Lake Mansarovar) -> enters Pakistan in GB",
        "path": "GB -> KPK -> Punjab -> Sindh -> Arabian Sea (Indus Delta)",
        "upstream": "Ladakh/GB (Skardu, Kharmong)",
        "downstream": "Kotri Barrage -> Indus Delta -> Arabian Sea",
        "confluences": ["Panjnad (Mithankot) - joins the combined 5 Punjab rivers", "Kabul River at Attock", "Gilgit River near Bunji", "Shyok River near Skardu"],
        "basin": "Indus main stem",
    },
    "Jhelum": {
        "source": "Verinag spring, Indian-administered Kashmir",
        "path": "AJK (Muzaffarabad) -> Punjab -> joins Chenab at Trimmu",
        "upstream": "Kashmir Valley / Wular Lake",
        "downstream": "Trimmu Barrage confluence with Chenab",
        "confluences": ["Neelum River at Muzaffarabad", "Chenab at Trimmu"],
        "basin": "Western river",
    },
    "Chenab": {
        "source": "Himachal Pradesh (Bara Lacha Pass area)",
        "path": "Enters Punjab near Marala -> joins Jhelum at Trimmu -> joins Sutlej/Panjnad system",
        "upstream": "Marala Headworks (entry point into Pakistan)",
        "downstream": "Trimmu -> Panjnad -> Indus at Mithankot",
        "confluences": ["Jhelum at Trimmu", "Ravi (indirectly via Panjnad system)"],
        "basin": "Western river",
    },
    "Ravi": {
        "source": "Himachal Pradesh (Bara Bhangal)",
        "path": "Enters Punjab near Lahore -> joins Chenab system downstream",
        "upstream": "Madhopur Headworks (India side)",
        "downstream": "Joins combined Panjnad system",
        "confluences": ["Chenab (via lower reaches)"],
        "basin": "Eastern river (largely diverted to India under IWT)",
    },
    "Sutlej": {
        "source": "Rakshastal Lake, Tibet",
        "path": "Punjab (mostly seasonal flow in Pakistan reach post-IWT)",
        "upstream": "Ropar/Ferozepur headworks (India side)",
        "downstream": "Joins Chenab via Panjnad",
        "confluences": ["Beas (in India, pre-Pakistan reach)", "Panjnad confluence"],
        "basin": "Eastern river (largely allocated to India under IWT)",
    },
    "Kabul River": {
        "source": "Sanglakh Range, Afghanistan",
        "path": "Enters KPK near Torkham -> Peshawar Valley -> joins Indus at Attock",
        "upstream": "Afghanistan (Kabul, Jalalabad)",
        "downstream": "Confluence with Indus at Attock",
        "confluences": ["Swat River near Charsadda", "Indus at Attock"],
        "basin": "Indus tributary (Kabul basin)",
    },
    "Swat River": {
        "source": "Hindu Kush foothills near Kalam",
        "path": "Swat Valley -> joins Kabul River near Charsadda",
        "upstream": "Kalam, Bahrain",
        "downstream": "Confluence with Kabul River",
        "confluences": ["Kabul River near Charsadda"],
        "basin": "Kabul basin",
    },
    "Hunza River": {
        "source": "Glacial meltwater, Karakoram (Batura, Hispar, Ultar glaciers)",
        "path": "Hunza Valley -> joins Gilgit River near Alam Bridge / Indus system",
        "upstream": "Khunjerab / Passu / Attabad",
        "downstream": "Joins Gilgit River -> Indus",
        "confluences": ["Gilgit River near Alam Bridge"],
        "basin": "Upper Indus (Karakoram glacial system)",
    },
    "Kurram River": {
        "source": "Paktia province, Afghanistan (Safed Koh range)",
        "path": "Enters KPK near Kurram district -> joins Indus near D.I. Khan area",
        "upstream": "Afghanistan (Paktia)",
        "downstream": "Confluence with Indus",
        "confluences": ["Indus River"],
        "basin": "Indus tributary (western hill-torrent system)",
    },
    "Gomal River": {
        "source": "Afghanistan (Sulaiman Range foothills)",
        "path": "South Waziristan/D.I. Khan -> joins Indus",
        "upstream": "Afghanistan / South Waziristan (feeds Gomal Zam Dam)",
        "downstream": "Confluence with Indus near D.I. Khan",
        "confluences": ["Indus River"],
        "basin": "Indus tributary (Sulaiman Range system)",
    },
    "Zhob River": {
        "source": "Toba Kakar Range, Balochistan",
        "path": "Zhob district -> joins Gomal River system toward the Indus",
        "upstream": "Toba Kakar Range foothills",
        "downstream": "Joins the Gomal system",
        "confluences": ["Gomal River"],
        "basin": "Indus tributary (Balochistan/Sulaiman system)",
    },
    "Hub River": {
        "source": "Kirthar Range foothills, Balochistan",
        "path": "Forms part of the Sindh-Balochistan border -> Arabian Sea near Karachi",
        "upstream": "Kirthar Range", "downstream": "Arabian Sea (Hub Dam reservoir en route)",
        "confluences": ["Arabian Sea"],
        "basin": "Independent coastal basin (not part of the Indus system)",
    },
    "Dasht River": {
        "source": "Central Makran hills, Balochistan",
        "path": "Turbat area -> Arabian Sea near Gwadar (feeds Mirani Dam)",
        "upstream": "Central Makran range", "downstream": "Arabian Sea near Gwadar",
        "confluences": ["Arabian Sea"],
        "basin": "Independent Makran coastal basin (not part of the Indus system)",
    },
}

# ---------------------------------------------------------------------------
# DAMS, BARRAGES/HEADWORKS, LINK CANALS
# ---------------------------------------------------------------------------
DAMS = [
    {"name": "Tarbela Dam", "river": "Indus", "province": "KPK", "type": "Earth-fill dam",
     "purpose": "Irrigation storage + hydropower (~4,888 MW installed, extensions ongoing)"},
    {"name": "Mangla Dam", "river": "Jhelum", "province": "AJK/Punjab border", "type": "Embankment dam",
     "purpose": "Irrigation storage + hydropower (~1,000+ MW)"},
    {"name": "Diamer-Bhasha Dam", "river": "Indus", "province": "GB/KPK border", "type": "RCC gravity dam (under construction)",
     "purpose": "Multipurpose: flood control, irrigation storage, ~4,500 MW planned hydropower"},
    {"name": "Kalabagh Dam (proposed, unbuilt)", "river": "Indus", "province": "Punjab/KPK border",
     "type": "Proposed gravity dam", "purpose": "Long-disputed multipurpose project; not constructed due to inter-provincial disagreement"},
    {"name": "Warsak Dam", "river": "Kabul River", "province": "KPK", "type": "Gravity dam",
     "purpose": "Irrigation + hydropower"},
    {"name": "Gomal Zam Dam", "river": "Gomal River", "province": "KPK", "type": "Earth-fill dam",
     "purpose": "Irrigation + hydropower + flood control"},
    {"name": "Mirani Dam", "river": "Dasht River", "province": "Balochistan", "type": "Earth-fill dam",
     "purpose": "Irrigation storage"},
]

BARRAGES = [
    {"name": "Marala Headworks", "river": "Chenab", "province": "Punjab", "note": "Chenab entry point into Pakistan; central to the Head Marala flow-reduction concerns raised by stakeholders."},
    {"name": "Rasool Barrage", "river": "Jhelum", "province": "Punjab", "note": "Feeds the Rasool-Qadirabad Link Canal."},
    {"name": "Qadirabad Barrage", "river": "Chenab", "province": "Punjab", "note": "Receiving end of the Rasool-Qadirabad Link Canal; feeds the Qadirabad-Balloki Link Canal."},
    {"name": "Balloki Barrage", "river": "Ravi", "province": "Punjab", "note": "Receiving end of the Qadirabad-Balloki Link Canal; feeds the Balloki-Sulemanki Link Canal."},
    {"name": "Sulemanki Headworks", "river": "Sutlej", "province": "Punjab", "note": "Receiving end of the Balloki-Sulemanki Link Canal, near the India border."},
    {"name": "Sidhnai Barrage", "river": "Ravi", "province": "Punjab", "note": "Receiving end of the Trimmu-Sidhnai Link Canal; feeds the Sidhnai-Melsi-Bahawalpur Link Canal."},
    {"name": "Melsi Headworks", "river": "Sutlej (Melsi Syphon)", "province": "Punjab", "note": "Part of the Sidhnai-Melsi-Bahawalpur link-canal chain."},
    {"name": "Trimmu Barrage", "river": "Chenab/Jhelum confluence", "province": "Punjab", "note": "Regulates combined Chenab-Jhelum flow; feeds the Trimmu-Sidhnai Link Canal."},
    {"name": "Panjnad Barrage", "river": "Panjnad", "province": "Punjab", "note": "Confluence point of the five Punjab rivers before joining the Indus; receiving end of the Taunsa-Panjnad Link Canal."},
    {"name": "Taunsa Barrage", "river": "Indus", "province": "Punjab", "note": "Feeds the Taunsa-Panjnad Link Canal."},
    {"name": "Chashma Barrage", "river": "Indus", "province": "Punjab", "note": "Feeds the Chashma-Jhelum Link Canal."},
    {"name": "Jinnah Barrage", "river": "Indus", "province": "Punjab", "note": "Near Kalabagh."},
    {"name": "Guddu Barrage", "river": "Indus", "province": "Sindh (upper)", "note": "First major barrage in Sindh."},
    {"name": "Sukkur Barrage", "river": "Indus", "province": "Sindh", "note": "Feeds seven canal commands, one of the world's largest irrigation networks."},
    {"name": "Kotri (Ghulam Muhammad) Barrage", "river": "Indus", "province": "Sindh", "note": "Last barrage before the Indus Delta; central to environmental-flow / delta-shrinkage debate."},
]

LINK_CANALS = [
    {"name": "Chashma-Jhelum (CJ) Link Canal", "connects": "Indus (Chashma) -> Jhelum"},
    {"name": "Rasool-Qadirabad (RQ) Link Canal", "connects": "Jhelum (Rasool) -> Chenab (Qadirabad)"},
    {"name": "Qadirabad-Balloki (QB) Link Canal", "connects": "Chenab (Qadirabad) -> Ravi (Balloki)"},
    {"name": "Balloki-Sulemanki (BS) Link Canal", "connects": "Ravi (Balloki) -> Sutlej (Sulemanki)"},
    {"name": "Trimmu-Sidhnai (TS) Link Canal", "connects": "Chenab (Trimmu) -> Ravi (Sidhnai)"},
    {"name": "Sidhnai-Melsi-Bahawalpur (SMB) Link Canal", "connects": "Ravi (Sidhnai) -> Sutlej (Melsi/Bahawalpur)"},
    {"name": "Taunsa-Panjnad (TP) Link Canal", "connects": "Indus (Taunsa) -> Panjnad"},
]

# ---------------------------------------------------------------------------
# LAKES (by province)
# ---------------------------------------------------------------------------
LAKES = [
    {"name": "Manchar Lake", "province": "Sindh", "type": "Freshwater (largest natural lake in Pakistan)"},
    {"name": "Keenjhar Lake", "province": "Sindh", "type": "Freshwater reservoir, drinking-water source for Karachi"},
    {"name": "Hamal Lake", "province": "Sindh", "type": "Wetland/lake complex"},
    {"name": "Saif-ul-Malook Lake", "province": "KPK", "type": "Glacial/alpine lake, Kaghan Valley"},
    {"name": "Attabad Lake", "province": "GB", "type": "Landslide-dammed lake formed in 2010 (Hunza River)"},
    {"name": "Satpara Lake", "province": "GB", "type": "Glacial lake near Skardu, also a reservoir"},
    {"name": "Shangrila (Lower Kachura) Lake", "province": "GB", "type": "Freshwater lake, Skardu"},
    {"name": "Borith Lake", "province": "GB", "type": "High-altitude saline lake, Gojal valley"},
    {"name": "Rawal Lake", "province": "ICT/Punjab border", "type": "Artificial reservoir, Islamabad water supply"},
    {"name": "Kallar Kahar Lake", "province": "Punjab", "type": "Salt Range lake"},
    {"name": "Hanna Lake", "province": "Balochistan", "type": "Reservoir near Quetta"},
]

# ---------------------------------------------------------------------------
# DESERTS
# ---------------------------------------------------------------------------
DESERTS = [
    {"name": "Thar Desert", "province": "Sindh", "note": "Largest desert in Pakistan, extends into India (Rajasthan)."},
    {"name": "Cholistan Desert", "province": "Punjab", "note": "Also called Rohi; adjoins Thar to the north."},
    {"name": "Thal Desert", "province": "Punjab", "note": "Between the Indus and Jhelum rivers."},
    {"name": "Kharan Desert", "province": "Balochistan", "note": "Arid basin in western Balochistan."},
]

# ---------------------------------------------------------------------------
# CLIMATE REGIONS
# ---------------------------------------------------------------------------
CLIMATE_REGIONS = {
    "Arid": "Most of Sindh, southern Punjab, much of Balochistan; low rainfall, high evapotranspiration.",
    "Tropical": "Coastal Sindh/Balochistan belt; hot, humid, cyclone/tidal-surge exposure.",
    "Temperate": "KPK valleys, AJK, Margalla foothills; four distinct seasons.",
    "Highland": "GB, northern KPK, AJK high mountains; cold winters, glacial influence.",
    "Polar": "Highest-altitude glaciated zones of the Karakoram/Himalaya (permanent snow/ice).",
}

# ---------------------------------------------------------------------------
# MOUNTAIN RANGES
# ---------------------------------------------------------------------------
MOUNTAIN_RANGES = {
    "Northern Highlands and Major Ranges": {
        "Karakoram Range": {
            "highest_peak": "K2 (Chhogori) - 8,611 m, 2nd highest peak on Earth",
            "location": "GB", "rivers": ["Indus", "Hunza", "Shigar", "Shyok"],
            "geology": "Young, tectonically active collision zone (India-Asia plate boundary); heavily glaciated.",
            "tourism": "Concordia trek, K2 base camp, Baltoro Glacier trekking, mountaineering expeditions.",
        },
        "Himalayas Range": {
            "highest_peak": "Nanga Parbat - 8,126 m (western anchor of the Himalayas)",
            "location": "GB/AJK border", "rivers": ["Indus", "Jhelum"],
            "geology": "Fold mountains from India-Eurasia collision; among the fastest-uplifting massifs on Earth.",
            "tourism": "Fairy Meadows, Nanga Parbat base camp trek.",
        },
        "Hindu Kush Range": {
            "highest_peak": "Tirich Mir - 7,708 m (highest peak outside the Karakoram/Himalaya in Pakistan)",
            "location": "Chitral, KPK", "rivers": ["Chitral/Kunar", "Yarkhun"],
            "geology": "Complex metamorphic/igneous terrain; seismically active.",
            "tourism": "Chitral Gol, Kalash Valleys, Shandur Pass (world's highest polo ground).",
        },
        "Hindu Raj Range": {
            "highest_peak": "Buni Zom - ~6,551 m",
            "location": "Between Chitral and Gilgit", "rivers": ["Yarkhun", "Ghizer"],
            "geology": "Transitional range linking Hindu Kush and Karakoram systems.",
            "tourism": "Remote trekking routes, Phander Valley access.",
        },
    },
    "Western and Southern Border Ranges": {
        "Spin Ghar (Koh-e-Safed)": {
            "highest_peak": "Sikaram - ~4,761 m",
            "location": "KPK/Afghanistan border", "rivers": ["Kurram"],
            "geology": "Folded sedimentary range along the Durand Line.",
            "tourism": "Limited; frontier region, historic Kurram Valley routes.",
        },
        "Sulaiman Mountains (Koh-e-Suleman)": {
            "highest_peak": "Takht-e-Sulaiman - ~3,487 m",
            "location": "Balochistan/Punjab/KPK border", "rivers": ["Gomal", "Zhob"],
            "geology": "Fold-and-thrust belt; hill-torrent flash-flood source for D.I. Khan/D.G. Khan.",
            "tourism": "Religious/historical trekking to Takht-e-Sulaiman.",
        },
        "Kirthar Range": {
            "highest_peak": "Kutte ji Qabar - ~2,168 m",
            "location": "Sindh/Balochistan border", "rivers": ["Hab River (nearby)"],
            "geology": "Limestone hills; low rainfall, sparse vegetation.",
            "tourism": "Kirthar National Park (wildlife, Sindh ibex/urial).",
        },
        "Toba Kakar Range": {
            "highest_peak": "Khalifat - ~3,487 m",
            "location": "Balochistan/Afghanistan border", "rivers": ["Zhob (headwaters)"],
            "geology": "Fold mountains, arid highland climate.",
            "tourism": "Ziarat Juniper forests, Quetta valley access.",
        },
        "Salt Range": {
            "highest_peak": "Sakesar - ~1,522 m",
            "location": "Northern Punjab", "rivers": ["Soan", "Indus (southern edge)"],
            "geology": "World-famous for Khewra Salt Mine; rich fossil and mineral deposits.",
            "tourism": "Khewra Salt Mine, Katas Raj Temples, Kallar Kahar.",
        },
    },
}

# ---------------------------------------------------------------------------
# FORESTS
# ---------------------------------------------------------------------------
FOREST_TYPES = {
    "Coniferous Forests": "Northern mountains, 1,000-4,000 m (KPK, GB) - pine, fir, deodar/cedar.",
    "Mangrove Forests": "Coastal wetlands of Karachi/Indus Delta and Balochistan coast (Arabian Sea).",
    "Riverain (Bela) Forests": "Narrow strips along the Indus riverbanks; tamarisk, poplar, willow.",
    "Tropical Thorn (Scrub) Forests": "Low-lying semi-arid plains of Punjab and Sindh; acacia/kikar-dominated.",
    "Irrigated/Planted Forests": "Man-made timber plantations, e.g. Changa Manga near Lahore.",
}

NOTABLE_FORESTS = [
    {"name": "Changa Manga Forest", "type": "Irrigated/Planted", "location": "Kasur district, Punjab (near Lahore)",
     "area": "~12,150 acres", "history": "Planted 1866 by the British as a managed timber plantation, one of the largest man-made forests in Asia.",
     "wildlife": "Deer park, peacocks, small mammals, birdlife.", "attractions": "Rail safari, boating, picnic areas, deer enclosure."},
    {"name": "Ziarat Juniper Forest", "type": "Coniferous (Juniper)", "location": "Ziarat, Balochistan",
     "area": "~110,000 acres (2nd largest juniper forest in the world)", "history": "Some juniper trees estimated at over 1,000-5,000 years old.",
     "wildlife": "Afghan urial, chukar partridge.", "attractions": "Quaid-e-Azam Residency, hiking, stargazing."},
    {"name": "Ushu Forest", "type": "Coniferous", "location": "Kalam/Ushu Valley, Swat, KPK",
     "area": "Extensive valley forest cover", "history": "Traditional Kohistani/Swati community forest use.",
     "wildlife": "Markhor, black bear, monal pheasant.", "attractions": "Trekking towards Mahodand Lake and Matiltan."},
    {"name": "Dir Forest", "type": "Coniferous", "location": "Upper/Lower Dir, KPK",
     "area": "Among KPK's largest natural conifer stands", "history": "Long-standing timber and watershed forest.",
     "wildlife": "Leopard, monkeys, pheasants.", "attractions": "Kumrat Valley access."},
    {"name": "Soon Valley Forest", "type": "Scrub/Sub-tropical", "location": "Khushab district, Salt Range, Punjab",
     "area": "Valley-wide forest and wetland mosaic", "history": "Traditional agro-pastoral landscape around Khabbeki/Uchhali lake wetlands.",
     "wildlife": "Migratory waterfowl, chinkara gazelle.", "attractions": "Lakes, terraced fields, hiking."},
    {"name": "Mukshpuri Forest", "type": "Coniferous", "location": "Nathiagali, KPK",
     "area": "Part of the Ayubia forest complex", "history": "Colonial-era hill-station forest reserve.",
     "wildlife": "Leopard, Kashmir flying squirrel, pheasants.", "attractions": "Mukshpuri Top hiking trail."},
    {"name": "Rama Meadows Forest", "type": "Coniferous/Alpine meadow", "location": "Near Astore, GB",
     "area": "Meadow-forest transition zone below Nanga Parbat", "history": "Traditional summer grazing (alpine pasture) area.",
     "wildlife": "Himalayan ibex, snow leopard (rare).", "attractions": "Nanga Parbat viewpoint, camping."},
    {"name": "Kalam Forest", "type": "Coniferous", "location": "Kalam, Swat, KPK",
     "area": "Extensive valley-side conifer cover", "history": "Historic timber source for Swat valley.",
     "wildlife": "Musk deer, snow leopard (higher elevations).", "attractions": "Gateway to Mahodand/Kundol lakes."},
    {"name": "Chitral Forests", "type": "Coniferous/dry temperate", "location": "Chitral, KPK",
     "area": "Scattered valley forests across Chitral district", "history": "Managed under community/Kalasha customary forest use.",
     "wildlife": "Markhor (Chitral Gol), snow leopard.", "attractions": "Chitral Gol National Park, Kalash valleys."},
    {"name": "Margalla Hills Scrub Forests", "type": "Sub-tropical scrub", "location": "Islamabad, ICT",
     "area": "Part of Margalla Hills National Park (~17,386 ha)", "history": "Protected since 1980 to conserve the capital's watershed.",
     "wildlife": "Leopard (rare), barking deer, grey goral, over 250 bird species.", "attractions": "Trail 3/5, Daman-e-Koh, Monal restaurant viewpoint."},
]

# ---------------------------------------------------------------------------
# NATIONAL PARKS (with lat/lon in coordinates.py)
# ---------------------------------------------------------------------------
NATIONAL_PARKS = [
    "Ayub National Park", "Jallo Park Lahore", "Lulusar-Dudipatsar National Park",
    "Lal Suhanra National Park", "Kirthar National Park", "Khunjerab National Park",
    "City Park Multan", "Kashmir Park", "DHA Park Multan", "Chitral Gol National Park",
    "Chaman Zar-e-Askari Park Multan", "Jinnah Park", "Hingol National Park",
    "Shakarparian National Park", "Faisal Park Mumtazabad", "Pir Lasura National Park",
    "Hazarganji-Chiltan National Park", "Pakistan Park", "Machiara National Park",
    "Rajana Forest Bhagat Wildlife Park", "Margalla Hills National Park",
]

# ---------------------------------------------------------------------------
# DISASTER RISK PROFILE
# ---------------------------------------------------------------------------
HAZARD_PROFILE = {
    "Hydro-meteorological": [
        "Riverine Floods", "Flash Floods / Hill Torrents", "Urban Flooding", "Mudflows",
        "Cloudbursts", "Monsoon Variability", "Droughts", "GLOFs", "Heatwaves", "Water Stress",
    ],
    "Tectonic": [
        "Earthquakes", "Landslides", "Avalanches", "Tsunamis", "Seismic Activity & Land Shifts", "Snow Contingencies",
    ],
    "Climatological & Emerging": [
        "Accelerated Glacier Melt", "Sea-Level Rise & Cyclones", "Smog",
        "Pollution (Air, Water, Soil)", "Erratic/Unpredictable Global Climate Patterns",
    ],
    "Anthropogenic": [
        "Industrial Accidents & Chemical Spills", "Transport & Infrastructure Risks", "Maritime Disasters",
        "Oil Spills", "Fires", "Encroachments", "Food Security", "Population Bulge", "Biological Hazards",
    ],
}

EXPOSURE_VULNERABILITY = {
    "Population Pressure and Diverse Terrains": "Rapid urbanization onto floodplains and hill-torrent fans.",
    "Vulnerable Settlements and Infrastructure Deficits": "Informal settlements, weak drainage/building codes.",
    "Institutional Vulnerabilities": ["Delayed Decision-Making", "Operational Confusion", "Public Distrust", "Resource Misallocation"],
    "Socio-Economic Stratification": ["Poverty", "Income inequality", "Limited access to education/healthcare/emergency resources",
                                       "Resource disparities", "Spatial entrapment", "Unequal mobility", "Marginalized communities", "Institutional neglect"],
}

EMERGING_RISK_TRENDS = {
    "Climate Risk Index": "Pakistan is repeatedly ranked among the countries most affected by extreme weather in the Global Climate Risk Index (CRI).",
    "GLOF Risk": "Rising temperatures are destabilising moraine-dammed glacial lakes in GB and northern KPK; past events include the 2025 Taalidass/Ghizer Lake outburst and the 2010 Attabad Lake landslide-dam event. Remote sensing, in-situ hydrological monitoring and early-warning systems are priority mitigations.",
    "Erratic Monsoon": "Early onset/extended seasons, uneven 'short-burst' rainfall distribution, and localized cloudbursts/hailstorms are increasing flash-flood, mudflow and soil-erosion risk.",
    "Sea Intrusion & Coastal Salinization": "Along Pakistan's ~1,050 km coastline, rising sea levels and saltwater intrusion threaten Karachi, Gwadar and Thatta; mangrove restoration and storm-surge early warning are key mitigations.",
}

RISK_SCENARIOS = {
    "Baseline": "Current hazard exposure with existing infrastructure and warning systems; localized, manageable disruption.",
    "Medium": "Elevated hazard frequency/intensity (e.g. an above-normal monsoon or a GLOF event) straining response capacity in one or more basins.",
    "Worst-Case": "Compound/cascading hazards (e.g. simultaneous upstream flood release + monsoon peak + infrastructure failure) overwhelming regional response capacity.",
}

# ---------------------------------------------------------------------------
# AGRO-ECONOMIC: crop seasons, apiculture, aquaculture
# ---------------------------------------------------------------------------
RABI_CROPS = [
    {"season": "Rabi", "crop": "Wheat", "typical_window": "Oct-Nov sowing / Apr-May harvest", "engineering_water_note": "Peak canal demand at sowing; sensitive to Nov-Dec flow availability."},
    {"season": "Rabi", "crop": "Gram (Chickpea)", "typical_window": "Oct-Nov sowing / Mar-Apr harvest", "engineering_water_note": "Largely rainfed/low irrigation demand."},
    {"season": "Rabi", "crop": "Mustard/Rapeseed", "typical_window": "Sep-Oct sowing / Feb-Mar harvest", "engineering_water_note": "Low-moderate irrigation requirement."},
    {"season": "Rabi", "crop": "Barley", "typical_window": "Oct-Nov sowing / Apr harvest", "engineering_water_note": "Drought-tolerant; grown in marginal/low-water zones."},
]

KHARIF_CROPS = [
    {"season": "Kharif", "crop": "Rice (incl. Basmati)", "typical_window": "May-Jul sowing / Oct-Nov harvest", "engineering_water_note": "Highest per-acre water demand crop; sensitive to canal closures and Chenab/Indus flow timing."},
    {"season": "Kharif", "crop": "Cotton", "typical_window": "Apr-May sowing / Oct-Dec harvest", "engineering_water_note": "Moderate-high water demand; critical irrigation window Jun-Aug."},
    {"season": "Kharif", "crop": "Sugarcane", "typical_window": "Feb-Apr (spring) or Sep (autumn) planting / 10-12 month crop", "engineering_water_note": "Year-round high water demand, overlaps both seasons."},
    {"season": "Kharif", "crop": "Maize", "typical_window": "Jul-Aug sowing / Oct-Nov harvest", "engineering_water_note": "Moderate irrigation demand; grown in both Punjab and KPK."},
]

APICULTURE = [
    {"indicator": "Managed bee colonies", "unit": "colonies", "description": "Number of managed honeybee (Apis mellifera / Apis cerana) colonies, concentrated in Punjab and KPK forest/agricultural belts."},
    {"indicator": "Honey production", "unit": "tonnes/year", "description": "Annual honey yield; linked to Sidr/berseem/citrus and forest floral sources."},
    {"indicator": "Beekeeper households", "unit": "households", "description": "Rural households engaged in apiculture as supplementary income."},
]

AQUACULTURE = [
    {"indicator": "Fish farm area", "unit": "hectares", "description": "Area under freshwater pond aquaculture, concentrated in Punjab and Sindh."},
    {"indicator": "Aquaculture production", "unit": "tonnes/year", "description": "Farmed fish output (major carp species) supplementing capture fisheries."},
    {"indicator": "Shrimp/coastal aquaculture", "unit": "tonnes/year", "description": "Brackish-water shrimp farming along the Sindh/Balochistan coast."},
]

# Editable, input-driven regional socio/agro dataset (baseline seed values;
# fully editable in the app via st.data_editor)
REGIONAL_AGRO_SOCIO_DATA = [
    {"province": "Punjab", "cultivated_area_ha": 12500000, "crop_production_tonnes": 38000000, "employment_persons": 9000000, "honey_production_tonnes": 3200, "aquaculture_production_tonnes": 55000},
    {"province": "Sindh", "cultivated_area_ha": 5600000, "crop_production_tonnes": 14500000, "employment_persons": 3800000, "honey_production_tonnes": 900, "aquaculture_production_tonnes": 38000},
    {"province": "KPK", "cultivated_area_ha": 1900000, "crop_production_tonnes": 4200000, "employment_persons": 1600000, "honey_production_tonnes": 2100, "aquaculture_production_tonnes": 9000},
    {"province": "Balochistan", "cultivated_area_ha": 1800000, "crop_production_tonnes": 2100000, "employment_persons": 950000, "honey_production_tonnes": 300, "aquaculture_production_tonnes": 1200},
    {"province": "GB", "cultivated_area_ha": 90000, "crop_production_tonnes": 210000, "employment_persons": 140000, "honey_production_tonnes": 120, "aquaculture_production_tonnes": 400},
    {"province": "AJK", "cultivated_area_ha": 210000, "crop_production_tonnes": 480000, "employment_persons": 260000, "honey_production_tonnes": 180, "aquaculture_production_tonnes": 600},
]

METRIC_OPTIONS = {
    "Cultivated area (ha)": "cultivated_area_ha",
    "Crop production (tonnes)": "crop_production_tonnes",
    "Employment (persons)": "employment_persons",
    "Honey production (tonnes)": "honey_production_tonnes",
    "Aquaculture production (tonnes)": "aquaculture_production_tonnes",
}

# ---------------------------------------------------------------------------
# CPEC / HYDROPOWER PROJECTS
# ---------------------------------------------------------------------------
CPEC_HYDROPOWER = [
    {"name": "Karot Hydropower Project", "capacity_mw": 720, "river": "Jhelum", "status": "Operational (COD 2022)", "source": "https://cpec.gov.pk/project-details/16"},
    {"name": "Suki Kinari (SK) Hydropower Station", "capacity_mw": 884, "river": "Kunhar", "status": "Under commissioning", "source": "https://cpec.gov.pk/project-details/15"},
    {"name": "Kohala Hydropower Project", "capacity_mw": 1124, "river": "Jhelum", "status": "Under construction", "source": "https://www.cpec.gov.pk/project-details/23"},
    {"name": "Azad Pattan Hydropower Project", "capacity_mw": 700.7, "river": "Jhelum", "status": "Under construction", "source": "https://cpec.gov.pk/project-details/91"},
]

DIAMER_BHASHA = {
    "capacity_mw": 4500,
    "storage": "Large multi-purpose reservoir intended to add significant live storage to the Indus system",
    "status_note": "Joint WAPDA/CPEC-linked financing and construction arrangement; timelines for the power component have seen repeated adjustment ('power postponement') relative to the water-storage component.",
    "sources": ["https://wapda.gov.pk/diamer-basha-dam-project/", "https://www.ead.gov.pk/NewsDetail/ODI1M2E0ODYtMjkyMi00NzdkLWE2ODQtMDk5NWIwZGY4YmE1"],
}

# ---------------------------------------------------------------------------
# INTER-PROVINCIAL DISPUTE (Punjab vs Sindh) + IRSA/CCI mechanisms
# ---------------------------------------------------------------------------
PUNJAB_SINDH_DISPUTE = {
    "sindh_position": "As the lower riparian, Sindh states that upstream withdrawals and canal proposals reduce flows needed for irrigation, drinking water and the Indus Delta's ecological requirements.",
    "punjab_position": "As the upper riparian and largest population/agricultural base, Punjab states that its withdrawals are consistent with the 1991 Water Apportionment Accord and existing infrastructure entitlements.",
    "structural_gridlock": "Recurrent deadlock in technical committees over telemetry data, canal-command proposals (e.g. the paused Cholistan/Green Pakistan canal proposals) and seasonal shortage-sharing formulas.",
}

IRSA_CCI_MECHANISMS = {
    "IRSA": "Indus River System Authority - technocratic body responsible for apportioning water among provinces under the 1991 Accord; a split/tied technical vote among provincial members can produce deadlock.",
    "CCI": "Council of Common Interests - constitutional forum (Article 154) where inter-provincial disputes, including water apportionment, can be escalated for political resolution.",
    "Supreme Court": "Constitutional review avenue of last resort where IRSA/CCI mechanisms fail to resolve a dispute.",
    "notes": "A 2024-2026 restructuring debate over IRSA's voting/veto rules and conciliation procedures has been part of the recent inter-provincial friction.",
    "sources": ["https://www.cci.gov.pk/Detail/NDZhY2I2ZDUtZTgzNy00MWEzLWE2M2ItZjU2NTkyODc4ZGJm"],
}

# ---------------------------------------------------------------------------
# REFERENCES
# ---------------------------------------------------------------------------
REFERENCES = [
    {"label": "PCA - Indus Waters Western Rivers Arbitration (Pakistan v. India)", "url": "https://pca-cpa.org/en/cases/284/"},
    {"label": "PCA - June 2025 Supplemental Award on Competence", "url": "https://pca-cpa.org/en/news/pca-press-release-pca-case-no-2023-01-proceedings-under-the-indus-waters-treaty-islamic-republic-of-pakistan-v-republic-of-india-3/"},
    {"label": "PPIB - CPEC Projects (updated 30 Jun 2026)", "url": "https://www.ppib.gov.pk/cpec.html"},
    {"label": "CPEC - Energy Projects", "url": "https://cpec.gov.pk/energy"},
    {"label": "CPEC - Karot", "url": "https://cpec.gov.pk/project-details/16"},
    {"label": "CPEC - Suki Kinari", "url": "https://cpec.gov.pk/project-details/15"},
    {"label": "CPEC - Kohala", "url": "https://www.cpec.gov.pk/project-details/23"},
    {"label": "CPEC - Azad Pattan", "url": "https://cpec.gov.pk/project-details/91"},
    {"label": "WAPDA - Diamer Basha Dam", "url": "https://wapda.gov.pk/diamer-basha-dam-project/"},
    {"label": "Ministry of Economic Affairs - Diamer Basha clarification (29 Aug 2026)", "url": "https://www.ead.gov.pk/NewsDetail/ODI1M2E0ODYtMjkyMi00NzdkLWE2ODQtMDk5NWIwZGY4YmE1"},
    {"label": "CCI - Functions / Article 155", "url": "https://www.cci.gov.pk/Detail/NDZhY2I2ZDUtZTgzNy00MWEzLWE2M2ItZjU2NTkyODc4ZGJm"},
    {"label": "World Bank - Indus Basin groundwater / IBIS", "url": "https://www.worldbank.org/en/news/feature/2021/03/25/managing-groundwater-resources-in-pakistan-indus-basin"},
    {"label": "PCA - Press release, PCA Case No. 2023-01 (31 Jul 2026)", "url": "https://docs.pca-cpa.org/2026/08/e893c52f-2023-14-pca-press-release-dated-31-july-2026.pdf"},
]

SDG_MDG_ESG = {
    "SDG_focus": [
        {"goal": "SDG 2 - Zero Hunger", "relevance": "Crop production, food security indicators (Rabi/Kharif module)."},
        {"goal": "SDG 6 - Clean Water and Sanitation", "relevance": "Barrage/dam/canal infrastructure, water-quality indicators (EC, pH, DO)."},
        {"goal": "SDG 13 - Climate Action", "relevance": "GLOF risk, monsoon variability, sea-level rise modules."},
        {"goal": "SDG 14 - Life Below Water", "relevance": "Mangrove forests, coastal aquaculture, Indus Delta salinity."},
        {"goal": "SDG 15 - Life on Land", "relevance": "Forest types, national parks, mountain biodiversity."},
        {"goal": "SDG 1 - No Poverty", "relevance": "Socio-economic stratification / vulnerability module."},
    ],
    "MDG_legacy": "Several SDG water/food/poverty targets carry forward unmet Millennium Development Goal (MDG 1 & MDG 7) baselines from the 2000-2015 period.",
    "Vision2030_Pakistan": "References Pakistan's long-term planning documents (e.g. Vision 2025/2030 successors) emphasising water security, food security and climate resilience as national priorities.",
    "ISO_ESG_notes": "Relevant voluntary frameworks: ISO 14001 (environmental management), ISO 26000 (social responsibility), and standard ESG pillars (Environmental / Social / Governance) as applied to water infrastructure and agri-value-chain projects.",
}
