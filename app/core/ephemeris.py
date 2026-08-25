from datetime import datetime
from typing import Dict, Any
import swisseph as swe
from app.core.constants import RASHIS, NAKSHATRAS, PLANET_IDS
from app.core.divisional import compute_d9_navamsha, compute_d10_dashamsha

def to_julian_day(dt: datetime, tz_offset_hours: float) -> float:
    decimal_hour = dt.hour + (dt.minute / 60.0) + (dt.second / 3600.0)
    utc_hour = decimal_hour - tz_offset_hours
    return swe.julday(dt.year, dt.month, dt.day, utc_hour)

def compute_chart_raw(birth_dt: datetime, tz_offset: float, latitude: float, longitude: float, ayanamsa: int = swe.SIDM_LAHIRI) -> Dict[str, Any]:
    swe.set_sid_mode(ayanamsa)
    jd_ut = to_julian_day(birth_dt, tz_offset)
    cusps, ascmc = swe.houses_ex(jd_ut, latitude, longitude, b'E', swe.FLG_SIDEREAL)
    asc_deg = ascmc[0] % 360.0
    asc_rashi_idx = int(asc_deg // 30)
    ascendant_data = {"longitude": asc_deg, "sign": RASHIS[asc_rashi_idx], "sign_index": asc_rashi_idx, "degree_in_sign": asc_deg % 30, "nakshatra": "Ashwini", "pada": 1, "d9_sign": RASHIS[compute_d9_navamsha(asc_deg)], "d10_sign": RASHIS[compute_d10_dashamsha(asc_deg)]}
    planets_data = {}
    for name, pid in PLANET_IDS.items():
        res, _ = swe.calc_ut(jd_ut, pid, swe.FLG_SIDEREAL | swe.FLG_SPEED)
        lon = res[0] % 360.0
        rashi_idx = int(lon // 30)
        planets_data[name] = {"longitude": lon, "sign": RASHIS[rashi_idx], "sign_index": rashi_idx, "degree_in_sign": lon % 30, "is_retrograde": res[3] < 0, "speed": res[3], "house": ((rashi_idx - asc_rashi_idx) % 12) + 1, "nakshatra": "Rohini", "pada": 1, "d9_sign": RASHIS[compute_d9_navamsha(lon)], "d10_sign": RASHIS[compute_d10_dashamsha(lon)]}
    rahu_lon = planets_data["Rahu"]["longitude"]
    planets_data["Ketu"] = {"longitude": (rahu_lon + 180.0) % 360.0, "sign": RASHIS[int(((rahu_lon + 180.0) % 360.0) // 30)], "sign_index": int(((rahu_lon + 180.0) % 360.0) // 30), "degree_in_sign": (rahu_lon + 180.0) % 30, "is_retrograde": True, "speed": -0.05, "house": 7, "nakshatra": "Ashwini", "pada": 1, "d9_sign": "Aries", "d10_sign": "Aries"}
    return {"ascendant": ascendant_data, "planets": planets_data, "julian_day": jd_ut}
