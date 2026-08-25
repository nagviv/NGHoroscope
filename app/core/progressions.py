from datetime import datetime, timedelta
from typing import Dict, Any, List
import swisseph as swe
from app.core.constants import RASHIS
from app.core.ephemeris import compute_chart_raw

ASPECT_TYPES = {
    0: ("Conjunction", "Intense focus / New beginnings"),
    60: ("Sextile", "Harmonious opportunities"),
    90: ("Square", "Dynamic tension / Action-oriented challenge"),
    120: ("Trine", "Effortless flow / Fortunate alignment"),
    180: ("Opposition", "Culmination / Polar awareness")
}

def calculate_progressions(birth_dt: datetime, target_year: int, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    completed_years = target_year - birth_dt.year
    progressed_dt = birth_dt + timedelta(days=completed_years)
    
    natal_chart = compute_chart_raw(birth_dt, tz_offset, lat, lon)
    prog_chart = compute_chart_raw(progressed_dt, tz_offset, lat, lon)
    
    natal_sun_lon = natal_chart["planets"]["Sun"]["longitude"]
    prog_sun_lon = prog_chart["planets"]["Sun"]["longitude"]
    solar_arc_distance = (prog_sun_lon - natal_sun_lon) % 360.0
    
    solar_arc_planets = {}
    for p_name, p_data in natal_chart["planets"].items():
        arc_lon = (p_data["longitude"] + solar_arc_distance) % 360.0
        rashi_idx = int(arc_lon // 30.0)
        solar_arc_planets[p_name] = {
            "longitude": round(arc_lon, 3),
            "sign": RASHIS[rashi_idx],
            "degree_in_sign": round(arc_lon % 30.0, 2)
        }
        
    aspects = []
    for p_prog_name, p_prog_data in prog_chart["planets"].items():
        for p_nat_name, p_nat_data in natal_chart["planets"].items():
            diff = abs(p_prog_data["longitude"] - p_nat_data["longitude"]) % 360.0
            if diff > 180.0:
                diff = 360.0 - diff
            for angle, (aspect_name, meaning) in ASPECT_TYPES.items():
                if abs(diff - angle) <= 1.2:
                    aspects.append({
                        "progressed_planet": p_prog_name,
                        "natal_planet": p_nat_name,
                        "aspect": aspect_name,
                        "angle": angle,
                        "orb": round(abs(diff - angle), 2),
                        "signification": meaning
                    })
                    
    return {
        "target_year": target_year,
        "progressed_age": completed_years,
        "solar_arc_degrees": round(solar_arc_distance, 2),
        "progressed_planets": prog_chart["planets"],
        "solar_arc_planets": solar_arc_planets,
        "progressed_aspects": aspects
    }
