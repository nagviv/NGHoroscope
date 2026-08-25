from datetime import datetime, timedelta
from typing import List, Dict, Any
from app.core.constants import DASHA_LORDS, DASHA_YEARS

DAYS_PER_YEAR = 365.2425

def calculate_vimshottari(moon_longitude: float, birth_dt: datetime) -> List[Dict[str, Any]]:
    nak_span = 360.0 / 27.0
    moon_lon = moon_longitude % 360.0
    nak_idx = int(moon_lon // nak_span)
    deg_in_nak = moon_lon % nak_span
    start_lord_idx = nak_idx % 9
    first_lord = DASHA_LORDS[start_lord_idx]
    balance_years = DASHA_YEARS[first_lord] * (1.0 - (deg_in_nak / nak_span))
    
    timeline = []
    current_start = birth_dt
    first_end = current_start + timedelta(days=balance_years * DAYS_PER_YEAR)
    timeline.append({"lord": first_lord, "start_date": current_start.isoformat(), "end_date": first_end.isoformat(), "duration_years": round(balance_years, 3), "is_balance": True})
    
    current_start = first_end
    for i in range(1, 9):
        lord = DASHA_LORDS[(start_lord_idx + i) % 9]
        years = DASHA_YEARS[lord]
        end_date = current_start + timedelta(days=years * DAYS_PER_YEAR)
        timeline.append({"lord": lord, "start_date": current_start.isoformat(), "end_date": end_date.isoformat(), "duration_years": round(years, 3), "is_balance": False})
        current_start = end_date
    return timeline

def get_active_dasha(dasha_tree: List[Dict[str, Any]], target_dt: datetime) -> Dict[str, str]:
    target_iso = target_dt.isoformat()
    for md in dasha_tree:
        if md["start_date"] <= target_iso <= md["end_date"]:
            return {"mahadasha": md["lord"], "antardasha": md["lord"]}
    return {"mahadasha": "Unknown", "antardasha": "Unknown"}
