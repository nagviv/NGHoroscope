from typing import Dict, Any, List
from app.core.constants import RASHI_LORDS, PLANET_DIGNITIES

def detect_yogas(chart: Dict[str, Any]) -> List[Dict[str, Any]]:
    yogas = []
    planets = chart["planets"]
    asc = chart["ascendant"]
    
    def get_house_lord(house_num: int) -> str:
        return RASHI_LORDS[(asc["sign_index"] + (house_num - 1)) % 12]
    
    def is_kendra(h: int) -> bool:
        return h in [1, 4, 7, 10]

    # Gajakesari
    if (((planets["Jupiter"]["house"] - planets["Moon"]["house"]) % 12) + 1) in [1, 4, 7, 10]:
        yogas.append({
            "name": "Gajakesari Yoga",
            "category": "Wisdom & Enduring Reputation",
            "description": "Jupiter in a Kendra from Moon: grants intellect, nobility, and high public standing."
        })

    # Budhaditya
    if planets["Sun"]["house"] == planets["Mercury"]["house"]:
        yogas.append({
            "name": "Budhaditya Yoga",
            "category": "Intellect & Professional Acumen",
            "description": f"Sun & Mercury conjoined in house {planets['Sun']['house']}: sharp analytical intelligence."
        })

    # Pancha Mahapurusha
    mahapurushas = {
        "Mars": ("Ruchaka Yoga", "Physical courage and executive dominance"),
        "Mercury": ("Bhadra Yoga", "Intellectual genius and exceptional communication"),
        "Jupiter": ("Hamsa Yoga", "Spiritual wisdom and noble character"),
        "Venus": ("Malavya Yoga", "Aesthetic mastery and refined luxury"),
        "Saturn": ("Sasa Yoga", "Command over masses and enduring perseverance")
    }
    for p_name, (y_name, y_desc) in mahapurushas.items():
        p_data = planets[p_name]
        dignity = PLANET_DIGNITIES[p_name]
        if is_kendra(p_data["house"]) and (p_data["sign_index"] == dignity["exalted"] or p_data["sign_index"] in dignity["own"]):
            yogas.append({
                "name": y_name,
                "category": "Pancha Mahapurusha Yoga",
                "description": f"{p_name} placed in Kendra in own/exalted sign: confers {y_desc}."
            })

    # Raja Yoga: 9th and 10th lords conjoined
    lord_9 = get_house_lord(9)
    lord_10 = get_house_lord(10)
    if planets[lord_9]["house"] == planets[lord_10]["house"]:
        yogas.append({
            "name": "Dharma-Karmadhipati Raja Yoga",
            "category": "High Executive Raja Yoga",
            "description": f"9th lord ({lord_9}) and 10th lord ({lord_10}) combine, granting professional eminence."
        })

    return yogas
