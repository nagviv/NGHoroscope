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

    if (((planets["Jupiter"]["house"] - planets["Moon"]["house"]) % 12) + 1) in [1, 4, 7, 10]:
        yogas.append({"name": "Gajakesari Yoga", "category": "Wisdom & Reputation", "description": "Jupiter in Kendra from Moon."})

    if planets["Sun"]["house"] == planets["Mercury"]["house"]:
        yogas.append({"name": "Budhaditya Yoga", "category": "Intellect", "description": "Sun & Mercury conjunction."})

    mahapurushas = {
        "Mars": ("Ruchaka Yoga", "Courage"),
        "Mercury": ("Bhadra Yoga", "Genius"),
        "Jupiter": ("Hamsa Yoga", "Wisdom"),
        "Venus": ("Malavya Yoga", "Luxury"),
        "Saturn": ("Sasa Yoga", "Persistence")
    }
    for p_name, (y_name, y_desc) in mahapurushas.items():
        p_data = planets[p_name]
        dignity = PLANET_DIGNITIES[p_name]
        if is_kendra(p_data["house"]) and (p_data["sign_index"] == dignity["exalted"] or p_data["sign_index"] in dignity["own"]):
            yogas.append({"name": y_name, "category": "Pancha Mahapurusha", "description": f"{p_name} in Kendra: {y_desc}."})

    lord_9 = get_house_lord(9)
    lord_10 = get_house_lord(10)
    if planets[lord_9]["house"] == planets[lord_10]["house"]:
        yogas.append({"name": "Dharma-Karmadhipati Raja Yoga", "category": "Raja Yoga", "description": "9th and 10th lords conjoined."})

    return yogas
