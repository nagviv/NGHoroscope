from datetime import datetime
from app.models.requests import BirthDetailsRequest
from app.models.responses import PanchangResponse
from app.core.panchang import calculate_panchang_details

class PanchangService:
    @staticmethod
    def calculate_panchang(req: BirthDetailsRequest) -> PanchangResponse:
        dt = datetime(req.year, req.month, req.day, req.hour, req.minute, req.second)
        p = calculate_panchang_details(dt, req.timezone_offset, req.latitude, req.longitude)
        return PanchangResponse(
            date=dt.strftime("%Y-%m-%d %H:%M:%S"),
            tithi=p["tithi"],
            vara=p["vara"],
            nakshatra=p["nakshatra"],
            yoga_index=p["yoga_index"],
            rahu_kaal=p["rahu_kaal"]
        )
