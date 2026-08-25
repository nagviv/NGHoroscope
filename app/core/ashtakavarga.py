from typing import Dict, Any
from app.core.constants import RASHIS

def calculate_ashtakavarga(chart: Dict[str, Any]) -> Dict[str, Any]:
    planets = chart["planets"]
    sav_points = [28] * 12
    for p_name in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        p_sign = planets[p_name]["sign_index"]
        sav_points[p_sign] += 1
        sav_points[(p_sign + 3) % 12] += 1
        sav_points[(p_sign + 9) % 12] += 1
        sav_points[(p_sign + 10) % 12] -= 1
        
    sav_by_rashi = {RASHIS[i]: sav_points[i] for i in range(12)}
    return {
        "total_bindus": sum(sav_points),
        "sav_by_rashi": sav_by_rashi,
        "strongest_rashi": max(sav_by_rashi, key=sav_by_rashi.get),
        "weakest_rashi": min(sav_by_rashi, key=sav_by_rashi.get)
    }
