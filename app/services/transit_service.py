from datetime import datetime
from app.models.requests import TransitRequest
from app.models.responses import TransitResponse
from app.core.ephemeris import compute_chart_raw
from app.core.doshas import check_sade_sati

class TransitService:
    @staticmethod
    def calculate_transits(req: TransitRequest) -> TransitResponse:
        birth_dt = datetime(req.birth_details.year, req.birth_details.month, req.birth_details.day, req.birth_details.hour, req.birth_details.minute, req.birth_details.second)
        target_dt = datetime(req.target_year, req.target_month, req.target_day, 12, 0, 0)
        natal = compute_chart_raw(birth_dt, req.birth_details.timezone_offset, req.birth_details.latitude, req.birth_details.longitude)
        transit = compute_chart_raw(target_dt, req.birth_details.timezone_offset, req.birth_details.latitude, req.birth_details.longitude)
        asc_idx = natal["ascendant"]["sign_index"]
        moon_idx = natal["planets"]["Moon"]["sign_index"]
        return TransitResponse(
            transit_date=target_dt.strftime("%Y-%m-%d"),
            transit_planets=transit["planets"],
            transits_from_lagna={p: ((d["sign_index"] - asc_idx) % 12) + 1 for p, d in transit["planets"].items()},
            transits_from_moon={p: ((d["sign_index"] - moon_idx) % 12) + 1 for p, d in transit["planets"].items()},
            sade_sati_status=check_sade_sati(moon_idx, transit["planets"]["Saturn"]["sign_index"])
        )
