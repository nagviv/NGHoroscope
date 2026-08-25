from datetime import datetime
from app.models.requests import MatchMakingRequest
from app.models.responses import MatchMakingResponse
from app.core.ephemeris import compute_chart_raw
from app.core.doshas import check_mangal_dosha
from app.core.ashtakoota import calculate_ashtakoota
from app.core.constants import NAKSHATRAS

class MatchService:
    @staticmethod
    def calculate_compatibility(req: MatchMakingRequest) -> MatchMakingResponse:
        b_dt = datetime(req.bride.year, req.bride.month, req.bride.day, req.bride.hour, req.bride.minute, req.bride.second)
        g_dt = datetime(req.groom.year, req.groom.month, req.groom.day, req.groom.hour, req.groom.minute, req.groom.second)
        b_chart = compute_chart_raw(b_dt, req.bride.timezone_offset, req.bride.latitude, req.bride.longitude)
        g_chart = compute_chart_raw(g_dt, req.groom.timezone_offset, req.groom.latitude, req.groom.longitude)
        b_moon_sign = b_chart["planets"]["Moon"]["sign"]
        b_nak_idx = NAKSHATRAS.index(b_chart["planets"]["Moon"]["nakshatra"])
        g_moon_sign = g_chart["planets"]["Moon"]["sign"]
        g_nak_idx = NAKSHATRAS.index(g_chart["planets"]["Moon"]["nakshatra"])
        ashtakoota_res = calculate_ashtakoota(b_moon_sign, b_nak_idx, g_moon_sign, g_nak_idx)
        return MatchMakingResponse(ashtakoota=ashtakoota_res, bride_mangal_dosha=check_mangal_dosha(b_chart), groom_mangal_dosha=check_mangal_dosha(g_chart), overall_compatibility="Auspicious Compatibility")
