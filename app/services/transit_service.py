from datetime import datetime
from typing import Dict, Any
from app.models.requests import TransitRequest
from app.models.responses import TransitResponse
from app.core.ephemeris import compute_chart_raw
from app.core.doshas import check_sade_sati

class TransitService:
    @staticmethod
    def calculate_transits(req: TransitRequest) -> TransitResponse:
        birth_dt = datetime(req.birth_details.year, req.birth_details.month, req.birth_details.day,
                            req.birth_details.hour, req.birth_details.minute, req.birth_details.second)
        target_dt = datetime(req.target_year, req.target_month, req.target_day, 12, 0, 0)
        
        natal_chart = compute_chart_raw(birth_dt, req.birth_details.timezone_offset, req.birth_details.latitude, req.birth_details.longitude)
        transit_chart = compute_chart_raw(target_dt, req.birth_details.timezone_offset, req.birth_details.latitude, req.birth_details.longitude)
        
        asc_sign_idx = natal_chart["ascendant"]["sign_index"]
        moon_sign_idx = natal_chart["planets"]["Moon"]["sign_index"]
        
        from_lagna = {}
        from_moon = {}
        
        for p, d in transit_chart["planets"].items():
            t_sign_idx = d["sign_index"]
            from_lagna[p] = ((t_sign_idx - asc_sign_idx) % 12) + 1
            from_moon[p] = ((t_sign_idx - moon_sign_idx) % 12) + 1
            
        saturn_transit_sign = transit_chart["planets"]["Saturn"]["sign_index"]
        sade_sati = check_sade_sati(moon_sign_idx, saturn_transit_sign)
        
        return TransitResponse(
            transit_date=target_dt.strftime("%Y-%m-%d"),
            transit_planets=transit_chart["planets"],
            transits_from_lagna=from_lagna,
            transits_from_moon=from_moon,
            sade_sati_status=sade_sati
        )
