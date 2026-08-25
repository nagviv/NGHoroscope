from datetime import datetime
from app.models.requests import VarshaphalaRequest
from app.models.responses import VarshaphalaResponse
from app.core.varshaphala import calculate_varshaphala

class VarshaphalaService:
    @staticmethod
    def calculate_annual_chart(req: VarshaphalaRequest) -> VarshaphalaResponse:
        b = req.birth_details
        birth_dt = datetime(b.year, b.month, b.day, b.hour, b.minute, b.second)
        res = calculate_varshaphala(birth_dt, req.target_year, b.timezone_offset, b.latitude, b.longitude)
        return VarshaphalaResponse(target_year=res["target_year"], solar_return_date=res["solar_return_date"], varsha_ascendant=res["varsha_ascendant"], varsha_planets=res["varsha_planets"], muntha=res["muntha"], panchadhikaris=res["panchadhikaris"], varsheshwara=res["varsheshwara"], tajika_yogas=res["tajika_yogas"])
