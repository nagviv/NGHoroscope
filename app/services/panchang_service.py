from datetime import datetime
from app.models.requests import BirthDetailsRequest
from app.models.responses import PanchangResponse
from app.core.panchang import calculate_panchang_details

class PanchangService:
    @staticmethod
    def calculate_panchang(req: BirthDetailsRequest) -> PanchangResponse:
        p = calculate_panchang_details(datetime(req.year, req.month, req.day, req.hour, req.minute, req.second), req.timezone_offset, req.latitude, req.longitude)
        return PanchangResponse(date=f"{req.year}-{req.month:02d}-{req.day:02d}", tithi=p["tithi"], vara=p["vara"], nakshatra=p["nakshatra"], yoga_index=p["yoga_index"], rahu_kaal=p["rahu_kaal"])
