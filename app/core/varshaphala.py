from datetime import datetime, timedelta
from typing import Dict, Any, List
import swisseph as swe
from app.core.constants import RASHIS, RASHI_LORDS, PLANET_IDS
from app.core.ephemeris import compute_chart_raw, to_julian_day

def calculate_muntha(natal_asc_sign_idx: int, birth_year: int, target_year: int) -> Dict[str, Any]:
    completed_years = target_year - birth_year
    muntha_sign_idx = (natal_asc_sign_idx + completed_years) % 12
    return {"sign": RASHIS[muntha_sign_idx], "sign_index": muntha_sign_idx, "lord": RASHI_LORDS[muntha_sign_idx], "completed_years": completed_years}

def calculate_varshaphala(birth_dt: datetime, target_year: int, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    natal_chart = compute_chart_raw(birth_dt, tz_offset, lat, lon)
    approx_return_dt = birth_dt.replace(year=target_year)
    varsha_chart = compute_chart_raw(approx_return_dt, tz_offset, lat, lon)
    
    natal_asc_idx = natal_chart["ascendant"]["sign_index"]
    muntha = calculate_muntha(natal_asc_idx, birth_dt.year, target_year)
    varsha_asc_idx = varsha_chart["ascendant"]["sign_index"]
    
    panchadhikaris = {
        "Muntha Lord": muntha["lord"],
        "Natal Lagna Lord": RASHI_LORDS[natal_asc_idx],
        "Varsha Lagna Lord": RASHI_LORDS[varsha_asc_idx],
        "Dina/Ratri Lord": "Sun" if approx_return_dt.hour < 18 else "Moon",
        "Tri-Rashi Lord": RASHI_LORDS[(varsha_asc_idx + 4) % 12]
    }
    
    tajika_yogas = []
    if abs(varsha_chart["planets"]["Sun"]["house"] - varsha_chart["planets"]["Jupiter"]["house"]) in [3, 4, 7, 9]:
        tajika_yogas.append({"name": "Ithasala (Muthashila) Yoga", "planets": "Sun & Jupiter", "nature": "Auspicious Success", "description": "Harmonious aspect fulfilling major objectives."})

    return {
        "target_year": target_year,
        "solar_return_date": approx_return_dt.strftime("%Y-%m-%d %H:%M"),
        "varsha_ascendant": varsha_chart["ascendant"],
        "varsha_planets": varsha_chart["planets"],
        "muntha": muntha,
        "panchadhikaris": panchadhikaris,
        "varsheshwara": panchadhikaris["Varsha Lagna Lord"],
        "tajika_yogas": tajika_yogas
    }
