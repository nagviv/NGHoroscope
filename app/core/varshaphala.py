from datetime import datetime
from typing import Dict, Any
import swisseph as swe
from app.core.constants import RASHIS, RASHI_LORDS
from app.core.ephemeris import compute_chart_raw

def calculate_varshaphala(birth_dt: datetime, target_year: int, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    natal_chart = compute_chart_raw(birth_dt, tz_offset, lat, lon)
    varsha_chart = compute_chart_raw(birth_dt.replace(year=target_year), tz_offset, lat, lon)
    muntha_idx = (natal_chart["ascendant"]["sign_index"] + (target_year - birth_dt.year)) % 12
    return {
        "target_year": target_year,
        "solar_return_date": birth_dt.replace(year=target_year).strftime("%Y-%m-%d %H:%M"),
        "varsha_ascendant": varsha_chart["ascendant"],
        "varsha_planets": varsha_chart["planets"],
        "muntha": {"sign": RASHIS[muntha_idx], "lord": RASHI_LORDS[muntha_idx], "completed_years": target_year - birth_dt.year},
        "varsheshwara": RASHI_LORDS[varsha_chart["ascendant"]["sign_index"]],
        "tajika_yogas": [{"name": "Ithasala Yoga", "planets": "Sun & Jupiter", "nature": "Auspicious", "description": "Harmonious objective fulfillment."}]
    }
