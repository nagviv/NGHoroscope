import swisseph as swe

RASHIS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

RASHI_LORDS = [
    "Mars", "Venus", "Mercury", "Moon",
    "Sun", "Mercury", "Venus", "Mars",
    "Jupiter", "Saturn", "Saturn", "Jupiter"
]

PLANET_DIGNITIES = {
    "Sun": {"exalted": 0, "debilitated": 6, "own": [4]},
    "Moon": {"exalted": 1, "debilitated": 7, "own": [3]},
    "Mars": {"exalted": 9, "debilitated": 3, "own": [0, 7]},
    "Mercury": {"exalted": 5, "debilitated": 11, "own": [2, 5]},
    "Jupiter": {"exalted": 3, "debilitated": 9, "own": [8, 11]},
    "Venus": {"exalted": 11, "debilitated": 5, "own": [1, 6]},
    "Saturn": {"exalted": 6, "debilitated": 0, "own": [9, 10]}
}

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
    "Hasta", "Chitra", "Svati", "Vishakha", "Anuradha", "Jyeshtha",
    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta",
    "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

NAKSHATRA_LORDS = [
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury",
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury",
    "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"
]

PLANET_IDS = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mars": swe.MARS,
    "Mercury": swe.MERCURY,
    "Jupiter": swe.JUPITER,
    "Venus": swe.VENUS,
    "Saturn": swe.SATURN,
    "Rahu": swe.MEAN_NODE
}

DASHA_LORDS = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]

DASHA_YEARS = {
    "Ketu": 7.0, "Venus": 20.0, "Sun": 6.0, "Moon": 10.0, "Mars": 7.0,
    "Rahu": 18.0, "Jupiter": 16.0, "Saturn": 19.0, "Mercury": 17.0
}

HOUSE_KARAKAS = {
    1: {"name": "Tanu Bhava (Self/Vitality)", "karakas": ["Sun"], "domains": ["Physique", "Health", "Identity"]},
    2: {"name": "Dhana Bhava (Wealth/Speech)", "karakas": ["Jupiter"], "domains": ["Savings", "Family lineage", "Speech"]},
    3: {"name": "Sahaja Bhava (Siblings/Courage)", "karakas": ["Mars"], "domains": ["Effort", "Courage", "Communication"]},
    4: {"name": "Sukha Bhava (Mother/Domestic Joy)", "karakas": ["Moon", "Venus"], "domains": ["Property", "Inner peace", "Mother"]},
    5: {"name": "Putra Bhava (Children/Intellect)", "karakas": ["Jupiter"], "domains": ["Intelligence", "Past-life merits", "Children"]},
    6: {"name": "Ari Bhava (Obstacles/Debts/Health)", "karakas": ["Mars", "Saturn"], "domains": ["Competition", "Service", "Healing"]},
    7: {"name": "Yuvati Bhava (Spouse/Partnerships)", "karakas": ["Venus"], "domains": ["Marriage", "Business contracts", "Alliances"]},
    8: {"name": "Randhra Bhava (Transformation/Longevity)", "karakas": ["Saturn"], "domains": ["Occult", "Sudden changes", "Research"]},
    9: {"name": "Dharma Bhava (Fortune/Higher Wisdom)", "karakas": ["Jupiter", "Sun"], "domains": ["Guru", "Higher learning", "Luck"]},
    10: {"name": "Karma Bhava (Profession/Status)", "karakas": ["Sun", "Mercury", "Saturn"], "domains": ["Career", "Public eminence", "Authority"]},
    11: {"name": "Labha Bhava (Gains/Aspirations)", "karakas": ["Jupiter"], "domains": ["Income streams", "Networks", "Elder siblings"]},
    12: {"name": "Vyaya Bhava (Expenditure/Liberation)", "karakas": ["Saturn", "Ketu"], "domains": ["Foreign residence", "Spirituality", "Sleep"]}
}
