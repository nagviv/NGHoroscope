from datetime import datetime
from app.models.requests import TransitRequest
from app.models.responses import KakshyaResponse
from app.core.kakshya import calculate_kakshya_transits

class KakshyaService:
    @staticmethod
    def calculate_kakshya_system(req: TransitRequest) -> KakshyaResponse:
        b = req.birth_details
        birth_dt = datetime(b.year, b.month, b.day, b.hour, b.minute, b.second)
        target_dt = datetime(req.target_year, req.target_month, req.target_day, 12, 0, 0)
        res = calculate_kakshya_transits(birth_dt, target_dt, b.timezone_offset, b.latitude, b.longitude)
        return KakshyaResponse(transit_date=res["transit_date"], kakshya_transits=res["kakshya_transits"])
