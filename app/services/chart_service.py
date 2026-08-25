from datetime import datetime
from app.models.requests import BirthDetailsRequest
from app.models.responses import NatalChartResponse
from app.core.ephemeris import compute_chart_raw
from app.core.dasha import calculate_vimshottari
from app.core.yogas import detect_yogas
from app.core.doshas import check_mangal_dosha, check_sade_sati, check_kaal_sarp_dosha
from app.core.ashtakavarga import calculate_ashtakavarga
from app.core.shadbala import calculate_shadbala_summary

class ChartService:
    @staticmethod
    def generate_natal_chart(req: BirthDetailsRequest) -> NatalChartResponse:
        birth_dt = datetime(req.year, req.month, req.day, req.hour, req.minute, req.second)
        raw = compute_chart_raw(birth_dt, req.timezone_offset, req.latitude, req.longitude)
        dasha_tree = calculate_vimshottari(raw["planets"]["Moon"]["longitude"], birth_dt)
        return NatalChartResponse(
            ascendant=raw["ascendant"], planets=raw["planets"],
            vargas={"D1_Rashi": {p: d["sign"] for p, d in raw["planets"].items()}},
            vimshottari_dasha=dasha_tree, yogas=detect_yogas(raw),
            doshas={"mangal_dosha": check_mangal_dosha(raw), "sade_sati": check_sade_sati(0, 0), "kaal_sarp": check_kaal_sarp_dosha(raw)},
            ashtakavarga=calculate_ashtakavarga(raw), shadbala=calculate_shadbala_summary(raw)
        )
