from datetime import datetime, timezone
from app.models.requests import AIQuestionRequest
from app.models.responses import AIAnswerResponse
from app.core.ephemeris import compute_chart_raw
from app.core.dasha import calculate_vimshottari, get_active_dasha

class AIService:
    @staticmethod
    def answer_question(req: AIQuestionRequest) -> AIAnswerResponse:
        birth_dt = datetime(req.birth_details.year, req.birth_details.month, req.birth_details.day, req.birth_details.hour, req.birth_details.minute, req.birth_details.second)
        natal = compute_chart_raw(birth_dt, req.birth_details.timezone_offset, req.birth_details.latitude, req.birth_details.longitude)
        dasha_tree = calculate_vimshottari(natal["planets"]["Moon"]["longitude"], birth_dt)
        active_dasha = get_active_dasha(dasha_tree, datetime.now(timezone.utc))
        return AIAnswerResponse(
            question=req.question,
            category=req.category or "General",
            active_dasha={"mahadasha": active_dasha["mahadasha"], "antardasha": active_dasha["antardasha"]},
            astrological_factors=[f"Lagna: {natal['ascendant']['sign']}", f"Active Dasha: {active_dasha['mahadasha']}"],
            analysis=f"Based on your {natal['ascendant']['sign']} Ascendant and active {active_dasha['mahadasha']} Mahadasha, this period favors structured execution.",
            practical_remedies=["Practice morning meditation", "Chant planetary seed mantras"]
        )
