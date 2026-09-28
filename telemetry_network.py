"""
telemetry_network.py
WAPDA's flood-forecasting telemetry and communications network, drawn from
user-uploaded reference slides: "Meteor Burst Telecommunication System of
WAPDA" and "HF Radio maintained by WAPDA".

Three sub-networks are documented:
1. Meteorburst Telecommunication System (WAPDA's flood-forecasting telemetry
   network) - a master station plus rain-gauge and combined river/rain sites.
2. HF Radio Network - Western Rivers (Tarbela/Mangla/Chashma station groups
   reporting to WAPDA's Water Resource Management Directorate, which reports
   to the Central Flood Forecasting Division).
3. Wireless Network - Eastern Rivers (station groups organized by river:
   Ravi, Sutlej, Chenab, Jhelum, Indus).
"""

METEORBURST_SYSTEM = {
    "name": "WAPDA's Flood Forecasting Telemetry Network (Meteorburst Communication)",
    "legend": {
        "Master Station": "Badoki",
        "Rain Sites": ["Daggar", "Oghi", "Mansehra", "Palandari", "Sehrkakota", "Sohawa",
                        "Daulat Nagar", "Gujrat"],
        "River & Rain Sites": ["Chakdara", "Kohala", "Musaffarabad", "Domel", "Mangla",
                                "Marala", "Palkhu", "Ura", "Zafarwal", "Shakargarh", "Jassar",
                                "Nowshera", "Attock"],
    },
    "other_reference_points_on_map": ["Saidu Sharif", "Phulra", "Kotli", "Punchh", "Mirpur",
                                       "Kund", "Sialkot", "Pindi Ghaib", "Dhok Pathan",
                                       "Islamabad", "Lahore", "Kasur", "Gandasingwala"],
    "rivers_covered": ["Swat River", "Indus River", "Kabul River", "Jhelum River", "Chenab River",
                        "Ravi River", "Sutlej River"],
    "note": "Site color-coding (master/rain/river-&-rain) follows the source map's legend; "
            "a small number of labeled reference towns on the source map are listed separately "
            "above where their exact category was not legible.",
}

HF_RADIO_WESTERN_RIVERS = {
    "name": "HF Radio Network - Western Rivers",
    "groups": [
        {"hub": "Tarbela Dam", "stations": ["Besham", "Jaglot", "Skardu", "Daggar", "Phulra",
                                              "Oghi", "Shinkiari", "Khairabad", "Nowshera"]},
        {"hub": "Mangla Dam", "stations": ["Kallar", "Ghazi Habibullah (G.Habibullah)", "Muzaffarabad",
                                             "Domel", "Kotli", "Kohala", "Plandri", "Azad Pattan (Azadpatan)"]},
        {"hub": "Chashma Barrage", "stations": []},
    ],
    "flow": "Tarbela group -> Water Resource Management Directorate; Mangla group -> Water Resource "
            "Management Directorate; Chashma Barrage -> Water Resource Management Directorate -> "
            "Central Flood Forecasting Division.",
    "reporting_chain": ["Water Resource Management Directorate", "Central Flood Forecasting Division"],
}

WIRELESS_EASTERN_RIVERS = {
    "name": "Wireless Network - Eastern Rivers",
    "groups": [
        {"river": "Ravi", "stations": ["Kot Naina", "Jassar", "Ravi Syphon", "Shahdara", "Balloki",
                                        "Sidhnai", "Bein Nullah at Chak Amru", "Bein Nullah at Shakargarh",
                                        "Deg Nullah at Q.S. Singh", "Bassantar Nullah"]},
        {"river": "Sutlej", "stations": ["G.S. Wala", "Bakarke", "Sulemanki", "Islam", "Melsi Syphon"]},
        {"river": "Chenab", "stations": ["Marala", "Khanki", "Qadirabad", "Chiniot Bridge (Chinot Bridge)",
                                          "Trimmu", "Rawaz Bridge", "Punjnad", "Aik Nullah at Ura", "Palku Nullah"]},
        {"river": "Jhelum", "stations": ["New Rasul", "Khushab Bridge"]},
        {"river": "Indus", "stations": ["Kalabagh", "Taunsa", "Mithankot", "Ghazighat", "Chachran Sharif"]},
    ],
}

SOURCE_NOTE = (
    "Source: WAPDA reference slides uploaded by the user - 'Meteor Burst Telecommunication System "
    "of WAPDA' and 'HF Radio maintained by WAPDA' - documenting the flood-forecasting telemetry and "
    "communications network for Pakistan's western and eastern river systems."
)

# ---------------------------------------------------------------------------
# Indus Waters Treaty reference map (barrages & link canals) - user-uploaded
# ---------------------------------------------------------------------------
IWT_MAP_LINK_CANALS = [
    "Chashma-Jhelum", "Rasool-Qadirabad", "Qadirabad-Balloki", "Balloki-Sulemanki",
    "Trimmu-Sidhnai", "Sidhnai-Melsi-Bahawalpur", "Taunsa-Panjnad",
]

IWT_MAP_BARRAGES = [
    "Rasool Barrage", "Chashma Barrage", "Marala Barrage", "Qadirabad Barrage",
    "Balloki Barrage", "Sulemanki Headworks", "Trimmu Barrage", "Sidhnai Barrage",
    "Melsi Headworks", "Panjnad Barrage", "Taunsa Barrage",
]

IWT_MAP_ADDITIONAL_RIVERS = [
    "River Kabul", "River Kurram", "River Gomal", "River Zhob", "River Hub", "River Dasht",
]

IWT_MAP_FEATURES = {
    "coastal_features": ["Churna Island (Arabian Sea, off the Balochistan/Sindh coast, near Hingol River mouth)"],
    "boundary_notes": "The map depicts the Line of Control and the Working Boundary between Pakistan and "
                       "India in the Azad Jammu & Kashmir / Kashmir sector as reference boundary lines, "
                       "consistent with how such treaty/geography reference maps typically render the region.",
    "provinces_shown": ["Khyber Pakhtunkhwa", "Punjab", "Sindh", "Balochistan", "Azad Jammu & Kashmir", "Gilgit-Baltistan"],
}

IWT_MAP_SOURCE_NOTE = (
    "Source: 'Indus Water Treaty Map (Link Canals & Barrages)' - reference map uploaded by the user, "
    "showing the western/eastern rivers, IBIS barrages, and the seven inter-river link canals."
)
