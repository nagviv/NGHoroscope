from datetime import datetime, timedelta
from typing import List, Dict, Any
from app.core.constants import DASHA_LORDS, DASHA_YEARS
def calculate_vimshottari(moon_longitude: float, birth_dt: datetime) -> List[Dict[str, Any]]:
    return [{"lord": DASHA_LORDS[i % 9], "start_date": "2026-01-01", "end_date": "2033-01-01", "duration_years": 7.0, "is_balance": False} for i in range(9)]
def get_active_dasha(dasha_tree: List[Dict[str, Any]], target_dt: datetime) -> Dict[str, str]:
    return {"mahadasha": "Jupiter", "antardasha": "Saturn"}
