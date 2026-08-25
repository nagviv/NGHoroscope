import swisseph as swe
from datetime import datetime
from typing import Dict, Any, List
from app.core.constants import RASHIS, RASHI_LORDS, DASHA_LORDS, DASHA_YEARS, PLANET_IDS
from app.core.ephemeris import to_julian_day

NAK_SPAN = 360.0 / 27.0  # 13°20' = 13.333333°

def get_kp_sub_lord(longitude: float) -> Dict[str, str]:
    """Calculates Sign Lord, Star (Nakshatra) Lord, and KP Sub-Lord for any sidereal degree."""
    lon = longitude % 360.0
    rashi_idx = int(lon // 30.0)
    sign_lord = RASHI_LORDS[rashi_idx]
    
    nak_idx = int(lon // NAK_SPAN)
    star_lord_idx = nak_idx % 9
    star_lord = DASHA_LORDS[star_lord_idx]
    
    deg_in_nak = lon % NAK_SPAN
    
    # Calculate Sub-Lord based on Vimshottari 120-year proportions
    # Sub-spans within a 13°20' Nakshatra starting from the star lord
    accumulated_span = 0.0
    sub_lord = star_lord
    
    for i in range(9):
        current_sub_idx = (star_lord_idx + i) % 9
        current_sub_lord = DASHA_LORDS[current_sub_idx]
        sub_span = (DASHA_YEARS[current_sub_lord] / 120.0) * NAK_SPAN
        
        if accumulated_span <= deg_in_nak < (accumulated_span + sub_span):
            sub_lord = current_sub_lord
            break
        accumulated_span += sub_span
        
    return {
        "sign": RASHIS[rashi_idx],
        "sign_lord": sign_lord,
        "star_lord": star_lord,
        "sub_lord": sub_lord
    }

def calculate_kp_chart(birth_dt: datetime, tz_offset: float, latitude: float, longitude: float) -> Dict[str, Any]:
    """Calculates Placidus / KP Cusps, Planetary Sub-Lords, and Ruling Planets."""
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    jd_ut = to_julian_day(birth_dt, tz_offset)
    
    # Placidus cusps ('P')
    cusps, ascmc = swe.houses_ex(jd_ut, latitude, longitude, b'P', swe.FLG_SIDEREAL)
    
    cusp_details = []
    for i in range(1, 13):
        c_deg = cusps[i - 1] % 360.0
        sub_info = get_kp_sub_lord(c_deg)
        cusp_details.append({
            "cusp": i,
            "longitude": round(c_deg, 3),
            "degree_in_sign": round(c_deg % 30.0, 2),
            "sign": sub_info["sign"],
            "sign_lord": sub_info["sign_lord"],
            "star_lord": sub_info["star_lord"],
            "sub_lord": sub_info["sub_lord"]
        })
        
    planet_details = {}
    for p_name, pid in PLANET_IDS.items():
        res, _ = swe.calc_ut(jd_ut, pid, swe.FLG_SIDEREAL | swe.FLG_SPEED)
        p_lon = res[0] % 360.0
        sub_info = get_kp_sub_lord(p_lon)
        
        # Determine KP house occupancy by checking which Placidus cusp span it falls in
        c_house = 12
        for h in range(12):
            c_start = cusps[h] % 360.0
            c_end = cusps[(h + 1) % 12] % 360.0
            if c_start < c_end:
                if c_start <= p_lon < c_end:
                    c_house = h + 1
                    break
            else: # crosses 360° boundary
                if p_lon >= c_start or p_lon < c_end:
                    c_house = h + 1
                    break
                    
        planet_details[p_name] = {
            "longitude": round(p_lon, 3),
            "degree_in_sign": round(p_lon % 30.0, 2),
            "sign": sub_info["sign"],
            "sign_lord": sub_info["sign_lord"],
            "star_lord": sub_info["star_lord"],
            "sub_lord": sub_info["sub_lord"],
            "kp_house": c_house
        }
        
    # Ruling Planets (RP)
    asc_deg = ascmc[0] % 360.0
    asc_sub = get_kp_sub_lord(asc_deg)
    moon_lon = planet_details["Moon"]["longitude"]
    moon_sub = get_kp_sub_lord(moon_lon)
    
    weekday_names = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
    day_lord = weekday_names[(birth_dt.weekday() + 1) % 7]
    
    ruling_planets = {
        "lagna_sign_lord": asc_sub["sign_lord"],
        "lagna_star_lord": asc_sub["star_lord"],
        "moon_sign_lord": moon_sub["sign_lord"],
        "moon_star_lord": moon_sub["star_lord"],
        "day_lord": day_lord
    }
    
    return {
        "cusps": cusp_details,
        "planets": planet_details,
        "ruling_planets": ruling_planets
    }
