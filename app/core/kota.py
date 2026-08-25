from datetime import datetime
from typing import Dict, Any
from app.core.constants import NAKSHATRAS, RASHI_LORDS
from app.core.ephemeris import compute_chart_raw

def calculate_kota_chakra(birth_dt: datetime, target_dt: datetime, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    natal_chart = compute_chart_raw(birth_dt, tz_offset, lat, lon)
    transit_chart = compute_chart_raw(target_dt, tz_offset, lat, lon)
    janma_idx = NAKSHATRAS.index(natal_chart["planets"]["Moon"]["nakshatra"])
    
    zones = {"Stambha (Pillar)": [], "Madhya (Inner)": [], "Prakara (Wall)": [], "Bahya (Outer)": []}
    for p_name, p_data in transit_chart["planets"].items():
        dist = (NAKSHATRAS.index(p_data["nakshatra"]) - janma_idx) % 27
        if dist in [0, 1, 2]: zones["Stambha (Pillar)"].append(p_name)
        elif dist in [3, 4, 5, 6]: zones["Madhya (Inner)"].append(p_name)
        elif dist in [7, 8, 9, 10, 11]: zones["Prakara (Wall)"].append(p_name)
        else: zones["Bahya (Outer)"].append(p_name)
        
    return {"transit_date": target_dt.strftime("%Y-%m-%d"), "kota_swami": RASHI_LORDS[natal_chart["planets"]["Moon"]["sign_index"]], "fortress_zones": zones, "defense_status": "Fortress Resilient"}
