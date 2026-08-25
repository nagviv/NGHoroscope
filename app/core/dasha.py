from datetime import datetime, timedelta
from typing import List, Dict, Any
from app.core.constants import DASHA_LORDS, DASHA_YEARS

DAYS_PER_YEAR = 365.2425

def calculate_vimshottari(moon_longitude: float, birth_dt: datetime) -> List[Dict[str, Any]]:
    """Calculates Mahadasha and Antardasha cycles for 120 years from birth."""
    nak_span = 360.0 / 27.0
    moon_lon = moon_longitude % 360.0
    nak_idx = int(moon_lon // nak_span)
    deg_in_nak = moon_lon % nak_span
    
    start_lord_idx = nak_idx % 9
    first_lord = DASHA_LORDS[start_lord_idx]
    
    traversed_ratio = deg_in_nak / nak_span
    balance_years = DASHA_YEARS[first_lord] * (1.0 - traversed_ratio)
    
    timeline = []
    current_start = birth_dt
    
    # Balance first Mahadasha
    first_duration_days = balance_years * DAYS_PER_YEAR
    first_end = current_start + timedelta(days=first_duration_days)
    
    timeline.append({
        "lord": first_lord,
        "start_date": current_start.isoformat(),
        "end_date": first_end.isoformat(),
        "duration_years": round(balance_years, 3),
        "is_balance": True
    })
    
    current_start = first_end
    
    # Subsequent 8 Mahadashas
    for i in range(1, 9):
        lord = DASHA_LORDS[(start_lord_idx + i) % 9]
        years = DASHA_YEARS[lord]
        duration_days = years * DAYS_PER_YEAR
        end_date = current_start + timedelta(days=duration_days)
        
        # Sub-period (Antardasha) breakdowns
        antardashas = []
        ad_start = current_start
        ad_start_idx = DASHA_LORDS.index(lord)
        
        for j in range(9):
            ad_lord = DASHA_LORDS[(ad_start_idx + j) % 9]
            ad_years = (years * DASHA_YEARS[ad_lord]) / 120.0
            ad_duration_days = ad_years * DAYS_PER_YEAR
            ad_end = ad_start + timedelta(days=ad_duration_days)
            
            antardashas.append({
                "lord": ad_lord,
                "start_date": ad_start.isoformat(),
                "end_date": ad_end.isoformat(),
                "duration_months": round(ad_years * 12.0, 2)
            })
            ad_start = ad_end

        timeline.append({
            "lord": lord,
            "start_date": current_start.isoformat(),
            "end_date": end_date.isoformat(),
            "duration_years": round(years, 3),
            "is_balance": False,
            "antardashas": antardashas
        })
        current_start = end_date
        
    return timeline
