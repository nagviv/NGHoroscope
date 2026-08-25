from datetime import datetime
from app.models.requests import MuhurtaRequest
from app.models.responses import MuhurtaResponse
from app.core.muhurta import calculate_muhurta_timeline

class MuhurtaService:
    @staticmethod
    def calculate_muhurta_details(req: MuhurtaRequest) -> MuhurtaResponse:
        dt = datetime(req.year, req.month, req.day, 12, 0, 0)
        res = calculate_muhurta_timeline(dt)
        return MuhurtaResponse(target_date=res["target_date"], choghadiya_day=res["choghadiya_day"], horas=res["horas"], special_spans=res["special_spans"], activity_suitability=res["activity_suitability"])
