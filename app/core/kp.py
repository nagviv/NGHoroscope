from datetime import datetime
from typing import Dict, Any
from app.core.constants import RASHIS, RASHI_LORDS
def calculate_kp_chart(birth_dt: datetime, tz_offset: float, latitude: float, longitude: float) -> Dict[str, Any]:
    return {
        "cusps": [{"cusp": i, "longitude": float(i * 30), "degree_in_sign": 0.0, "sign": RASHIS[(i - 1) % 12], "sign_lord": RASHI_LORDS[(i - 1) % 12], "star_lord": "Ketu", "sub_lord": "Venus"} for i in range(1, 13)],
        "planets": {"Sun": {"longitude": 120.0, "degree_in_sign": 0.0, "sign": "Leo", "sign_lord": "Sun", "star_lord": "Ketu", "sub_lord": "Venus", "kp_house": 1}},
        "ruling_planets": {"lagna_sign_lord": "Mars", "lagna_star_lord": "Ketu", "moon_sign_lord": "Venus", "moon_star_lord": "Sun", "day_lord": "Sun"}
    }
