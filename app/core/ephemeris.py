from datetime import datetime
from typing import Dict, Any
import swisseph as swe
from app.core.constants import RASHIS, NAKSHATRAS, PLANET_IDS
from app.core.divisional import compute_d9_navamsha, compute_d10_dashamsha

def to_julian_day(dt: datetime, tz_offset_hours: float) -> float:
    decimal_hour = dt.hour + (dt.minute / 60.0) + (dt.second / 3600.0)
    utc_hour = decimal_hour - tz_offset_hours
    day, month, year = dt.day, dt.month, dt.year
    if utc_hour < 0.0:
        utc_hour += 24.0
        day -= 1
    elif utc_hour >= 24.0:
        utc_hour -= 24.0
        day += 1
    return swe.julday(year, month, day, utc_hour)

def calculate_nakshatra(longitude: float) -> Dict[str, Any]:
    nak_span = 360.0 / 27.0
    pada_span = nak_span / 4.0
    lon = longitude % 360.0
    nak_idx = int(lon // nak_span)
    deg_in_nak = lon % nak_span
    return {
        "name": NAKSHATRAS[nak_idx],
        "index": nak_idx,
        "pada": int(deg_in_nak // pada_span) + 1,
        "progress_degrees": deg_in_nak
    }

def compute_chart_raw(birth_dt: datetime, tz_offset: float, latitude: float, longitude: float, ayanamsa: int = swe.SIDM_LAHIRI) -> Dict[str, Any]:
    swe.set_sid_mode(ayanamsa)
    jd_ut = to_julian_day(birth_dt, tz_offset)
    
    cusps, ascmc = swe.houses_ex(jd_ut, latitude, longitude, b'E', swe.FLG_SIDEREAL)
    asc_deg = ascmc[0] % 360.0
    asc_rashi_idx = int(asc_deg // 30)
    asc_nak = calculate_nakshatra(asc_deg)
    
    ascendant_data = {
        "longitude": asc_deg,
        "sign": RASHIS[asc_rashi_idx],
        "sign_index": asc_rashi_idx,
        "degree_in_sign": asc_deg % 30,
        "nakshatra": asc_nak["name"],
        "pada": asc_nak["pada"],
        "d9_sign": RASHIS[compute_d9_navamsha(asc_deg)],
        "d10_sign": RASHIS[compute_d10_dashamsha(asc_deg)]
    }
    
    planets_data = {}
    for name, pid in PLANET_IDS.items():
        res, _ = swe.calc_ut(jd_ut, pid, swe.FLG_SIDEREAL | swe.FLG_SPEED)
        lon = res[0] % 360.0
        speed = res[3]
        rashi_idx = int(lon // 30)
        nak = calculate_nakshatra(lon)
        house_num = ((rashi_idx - asc_rashi_idx) % 12) + 1
        
        planets_data[name] = {
            "longitude": lon,
            "sign": RASHIS[rashi_idx],
            "sign_index": rashi_idx,
            "degree_in_sign": lon % 30,
            "is_retrograde": speed < 0,
            "speed": speed,
            "house": house_num,
            "nakshatra": nak["name"],
            "pada": nak["pada"],
            "d9_sign": RASHIS[compute_d9_navamsha(lon)],
            "d10_sign": RASHIS[compute_d10_dashamsha(lon)]
        }
        
    rahu_lon = planets_data["Rahu"]["longitude"]
    ketu_lon = (rahu_lon + 180.0) % 360.0
    ketu_rashi_idx = int(ketu_lon // 30)
    ketu_nak = calculate_nakshatra(ketu_lon)
    ketu_house = ((ketu_rashi_idx - asc_rashi_idx) % 12) + 1
    
    planets_data["Ketu"] = {
        "longitude": ketu_lon,
        "sign": RASHIS[ketu_rashi_idx],
        "sign_index": ketu_rashi_idx,
        "degree_in_sign": ketu_lon % 30,
        "is_retrograde": planets_data["Rahu"]["is_retrograde"],
        "speed": planets_data["Rahu"]["speed"],
        "house": ketu_house,
        "nakshatra": ketu_nak["name"],
        "pada": ketu_nak["pada"],
        "d9_sign": RASHIS[compute_d9_navamsha(ketu_lon)],
        "d10_sign": RASHIS[compute_d10_dashamsha(ketu_lon)]
    }
    
    return {
        "ascendant": ascendant_data,
        "planets": planets_data,
        "julian_day": jd_ut
    }
