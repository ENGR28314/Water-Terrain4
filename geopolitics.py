"""
geopolitics.py
Indus Waters Treaty (IWT) dispute material.

IMPORTANT FRAMING NOTE FOR MAINTAINERS:
This module presents a live, contested bilateral legal/political dispute
between Pakistan and India. Content below is written as REPORTED POSITIONS
AND CLAIMS made by named parties (Pakistan, India, the Court of
Arbitration, the Neutral Expert process), with sources listed, rather than
as adjudicated fact. Where a claim is attributed to "Pakistan" or "India"
it means that party has stated it publicly / in proceedings - it is not
this dashboard's own conclusion. Update citations as the CoA / Neutral
Expert process develops.
"""

IWT_OVERVIEW = """
The Indus Waters Treaty (1960) governs water-sharing between Pakistan and India and
establishes the Permanent Indus Commission (PIC) as the treaty's regular channel for
data exchange, implementation review, and dispute resolution. Article VI requires the
Parties to exchange hydrological data (daily gauge/discharge readings, reservoir
releases, canal withdrawals), compiled and transmitted monthly and more frequently on
request. Article VIII designates the two Commissioners for Indus Waters, acting
through the PIC, as the treaty's regular channel of communication.
"""

TIMELINE_2025_2026 = [
    {"date": "May 2022", "event": "Last regular PIC meeting held in New Delhi."},
    {"date": "Apr 2025", "event": "India calls for IWT renegotiation and states aspects of treaty cooperation will be held 'in abeyance' (India's stated position)."},
    {"date": "27 Apr 2025", "event": "Reported sudden rise in Jhelum River levels causes flooding in Pakistan-administered Kashmir; Pakistan states India released water from Kashmir-side dams without prior PIC notification."},
    {"date": "Monsoon season 2025", "event": "India's High Commission conveys a River Tawi flood alert via diplomatic channels rather than through the PIC; India describes this as a humanitarian communication while maintaining the 'abeyance' position."},
    {"date": "31 Aug 2026", "event": "Court of Arbitration (CoA) issues an interim order restricting further concrete construction on Ratle's dam wall/intake above specified elevations pending the Neutral Expert's technical determination; India's government has stated it does not accept the CoA's jurisdiction and will continue construction on its own timeline."},
]

PAKISTAN_POSITION = """
Pakistan's stated position is that bypassing the PIC for data/alerts is inconsistent with
Articles VI and VIII, that a party cannot unilaterally suspend a treaty, and that the CoA is
a validly constituted forum under Article IX competent to hear these questions. Pakistan
has stated it will pursue PIC-level objections, and if unresolved, proceedings under
Annexure G of the treaty (Court of Arbitration), including potential interim-measures
requests, while continuing to raise the matter diplomatically.
"""

INDIA_POSITION = """
India's publicly stated position (as reported) is that flood alerts sent via diplomatic
channels were humanitarian communications, that treaty cooperation is 'in abeyance'
pending renegotiation, and - regarding the Court of Arbitration specifically - that India
does not recognize the CoA as validly constituted and does not consider itself bound by
its interim directions on the Ratle project; India's government has extended domestic
environmental clearance for Ratle through 2030 and stated it will continue construction
on its own schedule.
"""

# Technical dispute: Pakal Dul / Ratle (and related Kishanganga precedent)
TECHNICAL_DISPUTE_POINTS = [
    {
        "metric": "Pondage capacity (live storage)",
        "issue": "Volume of water a run-of-river plant may store behind the dam for daily peaking.",
        "pakistan_view": "Pondage should be minimal (Pakistan has proposed figures well below India's design values, e.g. far lower than India's ~24 MCM design at Ratle) to prevent flow manipulation.",
        "india_reported_design": "Larger pondage values (reported around 7.5 MCM at Kishanganga and ~24 MCM at Ratle) to support daily hydropower peaking.",
        "pakistan_concern": "Larger pondage could allow flow withholding during sowing season or sudden releases causing downstream flooding.",
    },
    {
        "metric": "Spillway design (orifice/gated vs. high-level/ungated)",
        "issue": "Low-level gated spillways are used to flush silt but can also allow rapid reservoir drawdown.",
        "pakistan_view": "Requests higher-level, minimally gated spillway configurations (Pakistan has requested the Ratle spillway crest be raised, reportedly by around 20 m).",
        "india_reported_design": "Deep, low-level orifice spillways to manage heavy Himalayan sediment loads.",
        "pakistan_concern": "Low gates could let an upstream state rapidly drain or restrict a reservoir, affecting downstream river levels.",
    },
    {
        "metric": "Intake submergence level",
        "issue": "How deep in the reservoir the power-tunnel intakes sit.",
        "pakistan_view": "Requests intakes raised (Pakistan has requested roughly 1.4 m at Kishanganga and up to about 8.8 m at Ratle).",
        "india_reported_design": "Deeper intakes to keep generating at low reservoir levels.",
        "pakistan_concern": "Deep intakes maximize operational flexibility for India at the potential expense of downstream flow consistency.",
    },
    {
        "metric": "Freeboard height",
        "issue": "Safety margin between max reservoir level and dam crest.",
        "pakistan_view": "Considers a smaller freeboard (around 1 m at Ratle) hydro-meteorologically sufficient.",
        "india_reported_design": "Reported design freeboard of about 2 m at Ratle.",
        "pakistan_concern": "Pakistan has characterized a larger freeboard as a possible way to hold more water than officially declared.",
    },
]

NEUTRAL_EXPERT_TIMELINE = [
    {"date": "Nov 2026", "milestone": "Synthesis memorandum to be distributed (per published Neutral Expert calendar)."},
    {"date": "Feb 2027", "milestone": "7th meeting and final hydraulic modelling exercise."},
    {"date": "Mar 2027", "milestone": "Circulation of the draft technical decision."},
    {"date": "Jul 2027", "milestone": "Issuance of the final, binding technical determination by the Neutral Expert (Michel Lino)."},
]

HEAD_MARALA_ISSUE = """
Stakeholder reports describe reduced Chenab flows at Head Marala and raise concerns about
potential downstream consequences for irrigation and crop yields in parts of Punjab. This
dashboard records these as stakeholder-reported concerns rather than as a verified
causal crop-loss estimate, because a quantified attribution would require a matched
hydrological (flow/discharge) dataset and agronomic yield dataset that has not been
compiled here. Treat figures in public commentary on this issue as claims pending
independent hydrological verification.
"""

INDIA_PROPOSED_CANAL_PROJECTS = """
Reported Indian proposals include feasibility studies for inter-basin transfer
infrastructure - described in public reporting as a canal system (cited length ~113 km)
intended to move water from the Indus system toward Punjab (India), Haryana and
Rajasthan, alongside proposed Chenab-to-Ravi-Beas-Sutlej and Ravi-Beas link canal
concepts, and continued construction of the Pakal Dul (1,000 MW), Ratle (850 MW),
Kiru (624 MW) and Kwar (540 MW) hydropower projects. These are reported plans/proposals
as described in public sources, not independently verified engineering facts in this
dashboard.
"""

COA_VALIDITY_NOTE = """
Pakistan has participated actively in Court of Arbitration proceedings and argues the CoA
is validly constituted under Article IX of the IWT. India's publicly stated position is
that it does not recognize the CoA's constitution or jurisdiction. This is an active,
unresolved point of disagreement between the parties; the dashboard does not take a
position on which view is legally correct.
"""

GEOPOLITICAL_SOURCES = [
    {"label": "PCA press release - Indus Waters Western Rivers Arbitration", "url": "https://pca-cpa.org/en/news/pca-press-release-pca-case-no-2023-01-the-indus-waters-western-rivers-arbitration-islamic-republic-of-pakistan-v-republic-of-india-4/"},
    {"label": "Dawn - coverage of proceedings", "url": "https://www.dawn.com/news/2028055"},
    {"label": "Athens Journal of Politics - Pratap, related analysis (PDF)", "url": "https://www.athensjournals.gr/politics/2026-7162-AJPIA-Pratap-02.pdf"},
    {"label": "PCA order on interim measures (PDF)", "url": "https://3vb.com/wp-content/uploads/2026/09/Order-on-Interim-Measures-Redacted.pdf"},
    {"label": "PCA press release, 31 Jul 2026 (PDF)", "url": "https://docs.pca-cpa.org/2026/08/e893c52f-2023-14-pca-press-release-dated-31-july-2026.pdf"},
    {"label": "Al Jazeera - Pakistan/Hague coverage", "url": "https://www.aljazeera.com/news/2026/9/1/pakistan-wins-indus-waters-battle-at-the-hague-but-india-threat-remains"},
    {"label": "ASIL - CoA finds IWT remains in force", "url": "https://asil.org/ilib/court-of-arbitration-finds-that-the-indus-water-treaty-remains-in-force/"},
    {"label": "Economic Times (India) - India rejects Hague tribunal direction on Ratle", "url": "https://government.economictimes.indiatimes.com/news/defence/indus-waters-treaty-india-rejects-hague-tribunals-directions-on-ratle-defends-hydropower-rights/133695497"},
    {"label": "Mongabay India - IWT modernisation debate", "url": "https://india.mongabay.com/2026/09/indus-water-treaty-needs-modernisation-experts-say-amid-deadlock/"},
    {"label": "Pak-Asia Youth Forum - Ratle dam transparency commentary", "url": "https://pakasiayouthforum.com/ratle-dam-treaty-transparency-test/"},
    {"label": "IDOS - Why the IWT must be abided by (commentary)", "url": "https://www.idos-research.de/en/the-current-column/article/why-the-indus-waters-treaty-must-be-abided-by/"},
    {"label": "Courthouse News - PCA press release coverage", "url": "https://courthousenews.com/wp-content/uploads/2026/08/pakistan-v-india-the-indus-water-western-rivers-arbitration-pca-press-release.pdf"},
    {"label": "Courthouse News - India 'business as usual' coverage", "url": "https://www.courthousenews.com/india-insists-business-as-usual-after-violating-water-treaty-with-pakistan/"},
    {"label": "Britannica - Indus Waters Treaty overview", "url": "https://www.britannica.com/event/Indus-Waters-Treaty"},
]

# ---------------------------------------------------------------------------
# 1947-1960 NEGOTIATION HISTORY
# Source: Biswas, A.K. (1992), "Indus Water Treaty: the Negotiating Process",
# Water International, 17(4), 201-209.
# ---------------------------------------------------------------------------
NEGOTIATION_HISTORY = [
    {"period": "1859-1900", "event": "Upper Bari Doab Canal (1859) and Sirhind Canal (1872) built; irrigated area in Sind roughly doubles (1.5M to 3.0M acres) between 1875-1900."},
    {"period": "Oct 1939", "event": "Sind formally requests a commission under the Government of India Act 1935 to review the impact of new Punjab irrigation schemes on its inundation canals."},
    {"period": "Sep 1941 - Jul 1942", "event": "The Indus Commission (chaired by Justice B.N. Rau) concludes Punjab withdrawals were likely to cause material injury to Sind's inundation canals; findings unacceptable to both provinces."},
    {"period": "1943-1947", "event": "Chief Engineers of Punjab and Bombay/Sind attempt an informal agreement (1943-45); dispute referred to the Secretary of State for India in London in early 1947."},
    {"period": "15 Aug 1947", "event": "Partition creates India and Pakistan before the British government can rule on the dispute, making the referral moot; the Radcliffe Commission's suggestion of joint Punjab water-system control is rejected by both Nehru and Jinnah."},
    {"period": "10 Dec 1947", "event": "Standstill Agreement between West and East Punjab Chief Engineers maintains pre-partition canal allocations until 31 March 1948."},
    {"period": "1 Apr 1948", "event": "India discontinues water delivery from Ferozepur Headworks to the Dipalpur Canal and UBDC branches after the Standstill Agreement lapses, precipitating the formal inter-country dispute."},
    {"period": "30 Apr 1948", "event": "Nehru orders East Punjab to resume water supply to the UBDC and reopen the Dipalpur Canal."},
    {"period": "4 May 1948", "event": "Delhi Agreement signed: India assures it will not suddenly withhold water; Pakistan recognizes India's need to develop water-scarce areas. Pakistan later calls it 'onerous and unsatisfactory' (16 Jun 1949) and claims it was signed under duress - a claim Nehru rejected in 1954."},
    {"period": "1950", "event": "Negotiations reach a near-total impasse; disputes remain over third-party adjudication (Pakistan wanted the ICJ; India preferred an ad hoc tribunal) and the Delhi Agreement's ad hoc payment sum."},
    {"period": "Feb 1951", "event": "David E. Lilienthal (former TVA chairman) visits India and Pakistan; his Collier's magazine article proposes joint, engineering-based development of the whole Indus system as a unit (TVA-style), financed in part by the World Bank."},
    {"period": "1951-1952", "event": "World Bank President Eugene R. Black takes up Lilienthal's proposal; both Nehru and Liaquat Ali Khan accept the Bank's process in principle. (Liaquat Ali Khan is assassinated 16 Oct 1951.)"},
    {"period": "May 1952", "event": "First Working Party meeting (Indian, Pakistani and World Bank engineers) held in Washington to scope a comprehensive Indus development plan."},
    {"period": "Oct 1953", "event": "India and Pakistan submit separate development/allocation plans to the Bank. India's plan: 29 MAF to India, 90 MAF to Pakistan. Pakistan's plan: 15.5 MAF to India, 102.5 MAF to Pakistan (of roughly similar ~118-119 MAF total usable water) - allocations differed widely though total-water estimates were close."},
    {"period": "5 Feb 1954", "event": "With the two national plans deadlocked, the World Bank puts forward its own proposal: the entire Western Rivers (Indus, Jhelum, Chenab) for Pakistan's exclusive use, and the entire Eastern Rivers (Ravi, Beas, Sutlej) for India's, with a transition period during which India continues historic Eastern-river supplies to Pakistan while replacement link canals are built."},
    {"period": "1954-1958", "event": "Pakistan gives qualified acceptance of the Bank proposal (28 Jul 1954); disputes continue over the adequacy/cost of replacement works. At a 1958 Rome meeting the Bank persuades Pakistan to place new storage on the Jhelum (for replacement) rather than only the Indus, reducing India's replacement-cost exposure."},
    {"period": "1958-1959", "event": "Pakistan proposes a development plan including Mangla Dam (Jhelum) and Tarbela Dam (Indus) at an estimated $1.12 billion; India presents a competing, cheaper alternative plan (Nov 1958) which Pakistan rejects, unwilling to depend on India for irrigation water."},
    {"period": "Aug 1959 - Sep 1960", "event": "Black assembles an international consortium (US, Canada, UK, West Germany, Australia, New Zealand) to fund the Indus Basin Development Fund; total Pakistan works cost set at $893.5 million (consortium grants $541M, Pakistan loans $150M + $315M supplemental, India's fixed contribution $174M)."},
    {"period": "19 Sep 1960", "event": "The Indus Waters Treaty is signed in Karachi by Indian PM Jawaharlal Nehru and Pakistani President Field Marshal Mohammad Ayub Khan; ratifications exchanged in Delhi, January 1961; the Treaty applied retroactively from 1 April 1960."},
]

TREATY_STRUCTURE_1960 = {
    "articles": 12, "paragraphs": 79, "annexes": 8, "annex_pages": 102,
    "eastern_rivers_allocation": "All waters of the Eastern Rivers (Sutlej, Beas, Ravi) allocated to India for unrestricted use, except that India had to continue supplying Pakistan per Annexure H during a 10-year transition period (1 Apr 1960 - 31 Mar 1970) while Pakistan built replacement works.",
    "western_rivers_allocation": "Pakistan received unrestricted use of the Western Rivers (Indus, Jhelum, Chenab), which India is 'under obligation to let flow' and may not interfere with, except for specified existing-use irrigation and a further ~701,000 acres of new irrigation development under specific conditions.",
    "india_replacement_contribution": "India agreed a fixed GBP 62 million contribution toward Pakistan's replacement-works cost, in 10 equal annual installments from 1960.",
    "article_vi": "Regular exchange of river and canal data between the two countries.",
    "article_vii": "Future cooperation between the parties.",
    "article_viii": "Establishes the permanent post of Commissioner of Indus Waters for each country - each to be 'a high-ranking engineer competent in the field of hydrology and water reuse' - the two Commissioners together constituting the Permanent Indus Commission (PIC), meeting at least once a year, alternating between India and Pakistan.",
    "pic_functions": ["Establish and promote cooperative arrangements for Treaty implementation",
                       "Promote cooperation between the Parties in developing the Indus system's waters",
                       "Examine and resolve by agreement any question on interpretation or implementation of the Treaty",
                       "Submit an annual report to both Governments before 1 June each year"],
    "article_ix_dispute_resolution": "If the Commission cannot resolve a specific problem, either side may refer it to a Neutral Expert under Annexure E; if the Neutral Expert cannot resolve it, a Court of Arbitration may be convened under Annexure G.",
}

NEGOTIATION_SOURCE_NOTE = (
    "Source: Biswas, A.K. (1992). 'Indus Water Treaty: the Negotiating Process.' Water International, "
    "17(4), 201-209. Uploaded by the user."
)
