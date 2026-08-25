from datetime import datetime
from app.models.requests import BirthDetailsRequest
from app.models.responses import JaiminiResponse
from app.core.ephemeris import compute_chart_raw
from app.core.jaimini import calculate_chara_karakas, calculate_chara_dasha_timeline

class JaiminiService:
    @staticmethod
    def calculate_jaimini_system(req: BirthDetailsRequest) -> JaiminiResponse:
        birth_dt = datetime(req.year, req.month, req.day, req.hour, req.minute, req.second)
        raw = compute_chart_raw(birth_dt, req.timezone_offset, req.latitude, req.longitude)
        karaka_data = calculate_chara_karakas(raw)
        chara_dasha = calculate_chara_dasha_timeline(raw, birth_dt)
        return JaiminiResponse(karakas=karaka_data["karakas"], atmakaraka_planet=karaka_data["atmakaraka_planet"], karakamsha_sign=karaka_data["karakamsha_sign"], arudha_lagna=karaka_data["arudha_lagna"], chara_dasha=chara_dasha)
