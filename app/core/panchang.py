from datetime import datetime
from typing import Dict, Any
from app.core.ephemeris import compute_chart_raw, calculate_nakshatra

TITHI_NAMES = ["Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shasthi", "Saptami", "Ashtami", "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima", "Amavasya"]
VARAS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def calculate_panchang_details(dt: datetime, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    chart = compute_chart_raw(dt, tz_offset, lat, lon)
    sun_lon = chart["planets"]["Sun"]["longitude"]
    moon_lon = chart["planets"]["Moon"]["longitude"]
    tithi_idx = int(((moon_lon - sun_lon) % 360.0) // 12.0)
    nak_info = calculate_nakshatra(moon_lon)
    weekday_idx = (dt.weekday() + 1) % 7
    return {"tithi": {"name": TITHI_NAMES[tithi_idx % len(TITHI_NAMES)], "paksha": "Shukla" if tithi_idx < 15 else "Krishna", "index": tithi_idx + 1}, "vara": VARAS[weekday_idx], "nakshatra": {"name": nak_info["name"], "pada": nak_info["pada"]}, "yoga_index": 1, "rahu_kaal": "16:30 - 18:00"}
