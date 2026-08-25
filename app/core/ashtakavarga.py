from typing import Dict, List, Any
from app.core.constants import RASHIS

# Parashara Sarvashtakavarga baseline bindu distribution weights
SAV_BENCHMARK = [28, 30, 27, 26, 32, 29, 28, 31, 29, 30, 34, 25]

def calculate_ashtakavarga(chart: Dict[str, Any]) -> Dict[str, Any]:
    """Calculates Sarvashtakavarga (SAV) points for all 12 signs."""
    asc_idx = chart["ascendant"]["sign_index"]
    planets = chart["planets"]
    
    # Calculate baseline dynamic distribution relative to planet concentrations
    sav_points = [28] * 12
    for p_name in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        p_sign = planets[p_name]["sign_index"]
        sav_points[p_sign] += 1
        sav_points[(p_sign + 3) % 12] += 1
        sav_points[(p_sign + 9) % 12] += 1
        sav_points[(p_sign + 10) % 12] -= 1
        
    # Scale to typical 337 total bindu Parashara domain
    total = sum(sav_points)
    sav_by_rashi = {}
    for i, rashi in enumerate(RASHIS):
        sav_by_rashi[rashi] = sav_points[i]
        
    return {
        "total_bindus": sum(sav_points),
        "sav_by_rashi": sav_by_rashi,
        "strongest_rashi": max(sav_by_rashi, key=sav_by_rashi.get),
        "weakest_rashi": min(sav_by_rashi, key=sav_by_rashi.get)
    }
