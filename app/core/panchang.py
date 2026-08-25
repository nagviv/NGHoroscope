from datetime import datetime
from typing import Dict, Any
from app.core.ephemeris import compute_chart_raw, calculate_nakshatra

TITHI_NAMES = [
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami", "Shasthi",
    "Saptami", "Ashtami", "Navami", "Dashami", "Ekadashi", "Dwadashi",
    "Trayodashi", "Chaturdashi", "Purnima",
    "Pratipada (Krishna)", "Dwitiya (Krishna)", "Tritiya (Krishna)", "Chaturthi (Krishna)",
    "Panchami (Krishna)", "Shasthi (Krishna)", "Saptami (Krishna)", "Ashtami (Krishna)",
    "Navami (Krishna)", "Dashami (Krishna)", "Ekadashi (Krishna)", "Dwadashi (Krishna)",
    "Trayodashi (Krishna)", "Chaturdashi (Krishna)", "Amavasya"
]

VARAS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def calculate_panchang_details(dt: datetime, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    chart = compute_chart_raw(dt, tz_offset, lat, lon)
    sun_lon = chart["planets"]["Sun"]["longitude"]
    moon_lon = chart["planets"]["Moon"]["longitude"]
    
    # 1. Tithi: (Moon - Sun) / 12 degrees
    diff = (moon_lon - sun_lon) % 360.0
    tithi_idx = int(diff // 12.0)
    tithi_name = TITHI_NAMES[tithi_idx % 30]
    paksha = "Shukla Paksha" if tithi_idx < 15 else "Krishna Paksha"
    
    # 2. Nakshatra
    nak_info = calculate_nakshatra(moon_lon)
    
    # 3. Vara (Weekday)
    weekday_idx = (dt.weekday() + 1) % 7 # Python Monday=0 -> Sun=0
    vara_name = VARAS[weekday_idx]
    
    # 4. Yoga: (Sun + Moon) / 13°20'
    yoga_span = 360.0 / 27.0
    yoga_idx = int(((sun_lon + moon_lon) % 360.0) // yoga_span)
    
    # 5. Rahu Kaal estimation based on weekday
    rahu_kaal_periods = [
        "16:30 - 18:00", # Sun
        "07:30 - 09:00", # Mon
        "15:00 - 16:30", # Tue
        "12:00 - 13:30", # Wed
        "13:30 - 15:00", # Thu
        "10:30 - 12:00", # Fri
        "09:00 - 10:30"  # Sat
    ]
    
    return {
        "tithi": {"name": tithi_name, "paksha": paksha, "index": tithi_idx + 1},
        "vara": vara_name,
        "nakshatra": {"name": nak_info["name"], "pada": nak_info["pada"]},
        "yoga_index": yoga_idx + 1,
        "rahu_kaal": rahu_kaal_periods[weekday_idx]
    }
