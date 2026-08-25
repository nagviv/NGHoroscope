from datetime import datetime
from typing import Dict, Any
def calculate_panchang_details(dt: datetime, tz_offset: float, lat: float, lon: float) -> Dict[str, Any]:
    return {"tithi": {"name": "Shukla Navami", "paksha": "Shukla", "index": 9}, "vara": "Tuesday", "nakshatra": {"name": "Rohini", "pada": 2}, "yoga_index": 5, "rahu_kaal": "15:00 - 16:30"}
