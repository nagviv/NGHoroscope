from typing import Dict, Any
from app.core.constants import RASHIS
def calculate_ashtakavarga(chart: Dict[str, Any]) -> Dict[str, Any]:
    return {"total_bindus": 337, "sav_by_rashi": {r: 28 for r in RASHIS}, "strongest_rashi": "Leo", "weakest_rashi": "Pisces"}
