from datetime import datetime
from typing import Dict, Any
from app.core.ephemeris import compute_chart_raw

KAKSHYA_LORDS = ["Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon", "Ascendant"]
KAKSHYA_SPAN = 30.0 / 8.0

def get_kakshya_details(degree_in_sign: float) -> Dict[str, Any]:
    deg = degree_in_sign % 30.0
    k_idx = min(int(deg // KAKSHYA_SPAN), 7)
    start_deg = k_idx * KAKSHYA_SPAN
    return {
        "kakshya_number": k_idx + 1,
        "kakshya_lord": KAKSHYA_LORDS[k_idx],
        "start_degree": round(start_deg, 2),
        "end_degree": round(start_deg + KAKSHYA_SPAN, 2)
    }

def calculate_kakshya_transits(birth_dt: datetime, target_dt: datetime, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    natal_chart = compute_chart_raw(birth_dt, tz_offset, lat, lon)
    transit_chart = compute_chart_raw(target_dt, tz_offset, lat, lon)
    transits = {}
    for p_name, p_data in transit_chart["planets"].items():
        k_info = get_kakshya_details(p_data["degree_in_sign"])
        has_bindu = ((p_data["sign_index"] + k_info["kakshya_number"]) % 2 == 0)
        transits[p_name] = {
            "sign": p_data["sign"],
            "degree_in_sign": round(p_data["degree_in_sign"], 2),
            "kakshya_number": k_info["kakshya_number"],
            "kakshya_lord": k_info["kakshya_lord"],
            "kakshya_span": f"{k_info['start_degree']}° - {k_info['end_degree']}°",
            "has_bindu": has_bindu,
            "fructification_status": "Auspicious Fruition" if has_bindu else "Low Fruition"
        }
    return {"transit_date": target_dt.strftime("%Y-%m-%d"), "kakshya_transits": transits}
