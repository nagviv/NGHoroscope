from datetime import datetime
from app.models.requests import BirthDetailsRequest
from app.models.responses import NatalChartResponse
from app.core.ephemeris import compute_chart_raw
from app.core.dasha import calculate_vimshottari
from app.core.yogas import detect_yogas
from app.core.doshas import check_mangal_dosha, check_sade_sati, check_kaal_sarp_dosha
from app.core.ashtakavarga import calculate_ashtakavarga

class ChartService:
    @staticmethod
    def generate_natal_chart(req: BirthDetailsRequest) -> NatalChartResponse:
        birth_dt = datetime(req.year, req.month, req.day, req.hour, req.minute, req.second)
        raw = compute_chart_raw(birth_dt, req.timezone_offset, req.latitude, req.longitude)
        
        moon_lon = raw["planets"]["Moon"]["longitude"]
        moon_sign_idx = raw["planets"]["Moon"]["sign_index"]
        
        dasha_tree = calculate_vimshottari(moon_lon, birth_dt)
        yogas = detect_yogas(raw)
        saturn_sign_idx = raw["planets"]["Saturn"]["sign_index"]
        
        doshas = {
            "mangal_dosha": check_mangal_dosha(raw),
            "sade_sati": check_sade_sati(moon_sign_idx, saturn_sign_idx),
            "kaal_sarp": check_kaal_sarp_dosha(raw)
        }
        ashtakavarga = calculate_ashtakavarga(raw)
        
        v_d1 = {"Ascendant": raw["ascendant"]["sign"]}
        v_d9 = {"Ascendant": raw["ascendant"]["d9_sign"]}
        v_d10 = {"Ascendant": raw["ascendant"]["d10_sign"]}
        for p, d in raw["planets"].items():
            v_d1[p] = d["sign"]
            v_d9[p] = d["d9_sign"]
            v_d10[p] = d["d10_sign"]
            
        return NatalChartResponse(
            ascendant=raw["ascendant"],
            planets=raw["planets"],
            vargas={"D1_Rashi": v_d1, "D9_Navamsha": v_d9, "D10_Dashamsha": v_d10},
            vimshottari_dasha=dasha_tree,
            yogas=yogas,
            doshas=doshas,
            ashtakavarga=ashtakavarga
        )
