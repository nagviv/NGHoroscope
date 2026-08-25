from typing import Dict, Any, List
from datetime import datetime, timedelta
from app.core.constants import RASHIS, RASHI_LORDS

KARAKA_NAMES = [
    ("Atmakaraka (AK)", "Soul signifier, primary life purpose, spiritual evolution"),
    ("Amatyakaraka (AmK)", "Career, intellect, executive power, professional success"),
    ("Bhratrikaraka (BK)", "Siblings, advisors, courage, spiritual masters"),
    ("Matrikaraka (MK)", "Mother, domestic stability, inner contentment, assets"),
    ("Putrakaraka (PK)", "Children, creativity, higher discernment, intelligence"),
    ("Gnatikaraka (GK)", "Obstacles, competition, disease, karmic tests"),
    ("Darakaraka (DK)", "Spouse, intimate partners, alliances, business relations")
]

def calculate_chara_karakas(chart: Dict[str, Any]) -> Dict[str, Any]:
    planets = chart["planets"]
    eligible = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
    sorted_planets = sorted(eligible, key=lambda p: planets[p]["degree_in_sign"], reverse=True)
    karaka_map = {}
    for idx, p_name in enumerate(sorted_planets):
        k_code, k_desc = KARAKA_NAMES[idx]
        karaka_map[k_code] = {
            "planet": p_name, "degree_in_sign": round(planets[p_name]["degree_in_sign"], 2),
            "sign": planets[p_name]["sign"], "d9_sign": planets[p_name]["d9_sign"],
            "house": planets[p_name]["house"], "signification": k_desc
        }
    ak_planet = sorted_planets[0]
    asc_sign_idx = chart["ascendant"]["sign_index"]
    lagna_lord = RASHI_LORDS[asc_sign_idx]
    lagna_lord_house = chart["planets"][lagna_lord]["house"]
    al_house = (((lagna_lord_house - 1) * 2) % 12) + 1
    if al_house in [1, 7]:
        al_house = ((al_house + 9) % 12) + 1
    return {
        "karakas": karaka_map, "atmakaraka_planet": ak_planet,
        "karakamsha_sign": planets[ak_planet]["d9_sign"],
        "arudha_lagna": {"house": al_house, "sign": RASHIS[(asc_sign_idx + (al_house - 1)) % 12]}
    }

def calculate_chara_dasha_timeline(chart: Dict[str, Any], birth_dt: datetime) -> List[Dict[str, Any]]:
    asc_sign_idx = chart["ascendant"]["sign_index"]
    direct_signs = [0, 1, 2, 6, 7, 8]
    is_direct = asc_sign_idx in direct_signs
    timeline = []
    current_start = birth_dt
    for i in range(12):
        sign_idx = (asc_sign_idx + i) % 12 if is_direct else (asc_sign_idx - i + 12) % 12
        sign_name = RASHIS[sign_idx]
        lord = RASHI_LORDS[sign_idx]
        lord_sign_idx = chart["planets"][lord]["sign_index"]
        duration_years = ((lord_sign_idx - sign_idx) % 12) if is_direct else ((sign_idx - lord_sign_idx) % 12)
        if duration_years == 0:
            duration_years = 12
        end_date = current_start + timedelta(days=duration_years * 365.2425)
        timeline.append({"sign": sign_name, "lord": lord, "duration_years": duration_years, "start_date": current_start.strftime("%Y-%m-%d"), "end_date": end_date.strftime("%Y-%m-%d")})
        current_start = end_date
    return timeline
