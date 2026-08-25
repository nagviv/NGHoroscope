from datetime import datetime
from app.models.requests import TransitRequest
from app.models.responses import TransitResponse
from app.core.ephemeris import compute_chart_raw

class TransitService:
    @staticmethod
    def calculate_transits(req: TransitRequest) -> TransitResponse:
        transit = compute_chart_raw(datetime(req.target_year, req.target_month, req.target_day, 12, 0, 0), req.birth_details.timezone_offset, req.birth_details.latitude, req.birth_details.longitude)
        return TransitResponse(transit_date=f"{req.target_year}-{req.target_month:02d}-{req.target_day:02d}", transit_planets=transit["planets"], transits_from_lagna={"Sun": 1}, transits_from_moon={"Sun": 1}, sade_sati_status={"is_active": False})
