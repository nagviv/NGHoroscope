from datetime import datetime
from app.models.requests import BirthDetailsRequest
from app.models.responses import KPResponse
from app.core.kp import calculate_kp_chart

class KPService:
    @staticmethod
    def calculate_kp_system(req: BirthDetailsRequest) -> KPResponse:
        birth_dt = datetime(req.year, req.month, req.day, req.hour, req.minute, req.second)
        kp_data = calculate_kp_chart(birth_dt, req.timezone_offset, req.latitude, req.longitude)
        return KPResponse(
            cusps=kp_data["cusps"],
            planets=kp_data["planets"],
            ruling_planets=kp_data["ruling_planets"]
        )
