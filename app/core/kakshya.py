from datetime import datetime
from typing import Dict, Any
from app.core.ephemeris import compute_chart_raw

KAKSHYA_LORDS = ["Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon", "Ascendant"]

def calculate_kakshya_transits(birth_dt: datetime, target_dt: datetime, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    transit_chart = compute_chart_raw(target_dt, tz_offset, lat, lon)
    transits = {}
    for p_name, p_data in transit_chart["planets"].items():
        k_idx = min(int((p_data["degree_in_sign"] % 30.0) // 3.75), 7)
        transits[p_name] = {"sign": p_data["sign"], "degree_in_sign": round(p_data["degree_in_sign"], 2), "kakshya_number": k_idx + 1, "kakshya_lord": KAKSHYA_LORDS[k_idx], "kakshya_span": f"{round(k_idx*3.75,2)}° - {round((k_idx+1)*3.75,2)}°", "fructification_status": "Auspicious"}
    return {"transit_date": target_dt.strftime("%Y-%m-%d"), "kakshya_transits": transits}
