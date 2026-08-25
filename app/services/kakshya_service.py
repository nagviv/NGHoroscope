from datetime import datetime
from app.models.requests import TransitRequest
from app.models.responses import KakshyaResponse
from app.core.kakshya import calculate_kakshya_transits

class KakshyaService:
    @staticmethod
    def calculate_kakshya_system(req: TransitRequest) -> KakshyaResponse:
        birth_dt = datetime(req.birth_details.year, req.birth_details.month, req.birth_details.day, req.birth_details.hour, req.birth_details.minute, req.birth_details.second)
        target_dt = datetime(req.target_year, req.target_month, req.target_day, 12, 0, 0)
        res = calculate_kakshya_transits(birth_dt, target_dt, req.birth_details.timezone_offset, req.birth_details.latitude, req.birth_details.longitude)
        return KakshyaResponse(
            transit_date=res["transit_date"],
            kakshya_transits=res["kakshya_transits"]
        )
