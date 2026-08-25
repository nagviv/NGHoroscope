from typing import Dict, Any, List
from app.core.constants import RASHI_LORDS, PLANET_DIGNITIES

def detect_yogas(chart: Dict[str, Any]) -> List[Dict[str, Any]]:
    yogas = []
    planets = chart["planets"]
    asc = chart["ascendant"]
    if (((planets["Jupiter"]["house"] - planets["Moon"]["house"]) % 12) + 1) in [1, 4, 7, 10]:
        yogas.append({"name": "Gajakesari Yoga", "category": "Wisdom & Reputation", "description": "Jupiter in Kendra from Moon."})
    if planets["Sun"]["house"] == planets["Mercury"]["house"]:
        yogas.append({"name": "Budhaditya Yoga", "category": "Intellect", "description": "Sun & Mercury conjunction."})
    return yogas
