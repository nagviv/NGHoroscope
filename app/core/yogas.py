from typing import Dict, Any, List
from app.core.constants import RASHIS, RASHI_LORDS, PLANET_DIGNITIES

def detect_yogas(chart: Dict[str, Any]) -> List[Dict[str, Any]]:
    yogas = []
    planets = chart["planets"]
    asc = chart["ascendant"]
    
    def get_house_lord(house_num: int) -> str:
        rashi_idx = (asc["sign_index"] + (house_num - 1)) % 12
        return RASHI_LORDS[rashi_idx]
    
    def is_kendra(h: int) -> bool:
        return h in [1, 4, 7, 10]

    # Gajakesari
    moon_house = planets["Moon"]["house"]
    jup_house = planets["Jupiter"]["house"]
    if (((jup_house - moon_house) % 12) + 1) in [1, 4, 7, 10]:
        yogas.append({
            "name": "Gajakesari Yoga",
            "category": "Wisdom & Enduring Reputation",
            "description": "Jupiter in a Kendra from the Moon, granting wisdom, respect, and intellectual vitality."
        })

    # Budhaditya
    if planets["Sun"]["house"] == planets["Mercury"]["house"]:
        yogas.append({
            "name": "Budhaditya Yoga",
            "category": "Intellect & Leadership",
            "description": "Sun and Mercury conjunction creating analytical sharp acumen."
        })

    # Pancha Mahapurusha
    mahapurushas = {
        "Mars": ("Ruchaka Yoga", "Physical courage, executive leadership"),
        "Mercury": ("Bhadra Yoga", "Analytical brilliance, eloquence"),
        "Jupiter": ("Hamsa Yoga", "Spiritual ethics, noble character"),
        "Venus": ("Malavya Yoga", "Aesthetic mastery, prosperity"),
        "Saturn": ("Sasa Yoga", "Mass leadership, persistence")
    }
    for p_name, (y_name, y_desc) in mahapurushas.items():
        p_data = planets[p_name]
        dignity = PLANET_DIGNITIES[p_name]
        if is_kendra(p_data["house"]) and (p_data["sign_index"] == dignity["exalted"] or p_data["sign_index"] in dignity["own"]):
            yogas.append({
                "name": y_name,
                "category": "Pancha Mahapurusha Yoga",
                "description": f"{p_name} placed in Kendra in own/exalted sign: {y_desc}."
            })

    # Raja Yogas
    lord_9 = get_house_lord(9)
    lord_10 = get_house_lord(10)
    if planets[lord_9]["house"] == planets[lord_10]["house"]:
        yogas.append({
            "name": "Dharma-Karmadhipati Raja Yoga",
            "category": "High Status Raja Yoga",
            "description": f"Conjunction of 9th lord ({lord_9}) and 10th lord ({lord_10}) signifying career eminence."
        })

    return yogas
