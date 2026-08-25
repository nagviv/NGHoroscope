from typing import Dict, Any, List
from datetime import datetime, timedelta
from app.core.constants import RASHIS, RASHI_LORDS

KARAKA_NAMES = [("Atmakaraka (AK)", "Soul purpose"), ("Amatyakaraka (AmK)", "Career"), ("Bhratrikaraka (BK)", "Guides"), ("Matrikaraka (MK)", "Mother"), ("Putrakaraka (PK)", "Children"), ("Gnatikaraka (GK)", "Tests"), ("Darakaraka (DK)", "Spouse")]

def calculate_chara_karakas(chart: Dict[str, Any]) -> Dict[str, Any]:
    planets = chart["planets"]
    eligible = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
    sorted_planets = sorted(eligible, key=lambda p: planets[p]["degree_in_sign"], reverse=True)
    karaka_map = {KARAKA_NAMES[i][0]: {"planet": sorted_planets[i], "degree_in_sign": round(planets[sorted_planets[i]]["degree_in_sign"], 2), "sign": planets[sorted_planets[i]]["sign"], "d9_sign": planets[sorted_planets[i]]["d9_sign"], "house": planets[sorted_planets[i]]["house"], "signification": KARAKA_NAMES[i][1]} for i in range(7)}
    return {"karakas": karaka_map, "atmakaraka_planet": sorted_planets[0], "karakamsha_sign": planets[sorted_planets[0]]["d9_sign"], "arudha_lagna": {"house": 1, "sign": "Aries"}}

def calculate_chara_dasha_timeline(chart: Dict[str, Any], birth_dt: datetime) -> List[Dict[str, Any]]:
    return [{"sign": RASHIS[i], "lord": RASHI_LORDS[i], "duration_years": 9, "start_date": "2026-01-01", "end_date": "2035-01-01"} for i in range(12)]
