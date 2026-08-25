from datetime import datetime
from typing import Dict, Any
from app.core.constants import NAKSHATRAS
from app.core.ephemeris import compute_chart_raw

def calculate_sarvatobhadra_chakra(birth_dt: datetime, target_dt: datetime, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    natal_chart = compute_chart_raw(birth_dt, tz_offset, lat, lon)
    transit_chart = compute_chart_raw(target_dt, tz_offset, lat, lon)
    natal_moon_nak = natal_chart["planets"]["Moon"]["nakshatra"]
    janma_idx = NAKSHATRAS.index(natal_moon_nak)
    
    sensitive_points = {
        "Janma Nakshatra": natal_moon_nak,
        "Karma (10th)": NAKSHATRAS[(janma_idx + 9) % 27],
        "Sanghatika (16th)": NAKSHATRAS[(janma_idx + 15) % 27],
        "Manasa (25th)": NAKSHATRAS[(janma_idx + 24) % 27]
    }
    
    vedhas = []
    for p_name, p_data in transit_chart["planets"].items():
        if p_data["nakshatra"] in sensitive_points.values():
            vedhas.append({"planet": p_name, "transit_nakshatra": p_data["nakshatra"], "target": "Janma Point", "vedha_type": "Front Vedha"})
            
    return {"transit_date": target_dt.strftime("%Y-%m-%d"), "sensitive_nakshatras": sensitive_points, "active_vedhas": vedhas, "defense_verdict": "Clear / No Adverse Vedha" if not vedhas else "Caution Advised"}
