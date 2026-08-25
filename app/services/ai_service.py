from datetime import datetime, timezone
from app.models.requests import AIQuestionRequest
from app.models.responses import AIAnswerResponse
from app.core.ephemeris import compute_chart_raw
from app.core.dasha import calculate_vimshottari, get_active_dasha
from app.core.yogas import detect_yogas
from app.core.doshas import check_sade_sati

class AIService:
    @staticmethod
    def answer_question(req: AIQuestionRequest) -> AIAnswerResponse:
        birth_dt = datetime(req.birth_details.year, req.birth_details.month, req.birth_details.day,
                            req.birth_details.hour, req.birth_details.minute, req.birth_details.second)
        natal = compute_chart_raw(birth_dt, req.birth_details.timezone_offset, req.birth_details.latitude, req.birth_details.longitude)
        dasha_tree = calculate_vimshottari(natal["planets"]["Moon"]["longitude"], birth_dt)
        now_dt = datetime.now(timezone.utc)
        active_dasha = get_active_dasha(dasha_tree, now_dt)
        yogas = detect_yogas(natal)
        transit = compute_chart_raw(now_dt, req.birth_details.timezone_offset, req.birth_details.latitude, req.birth_details.longitude)
        
        asc = natal["ascendant"]["sign"]
        moon = natal["planets"]["Moon"]["sign"]
        nak = natal["planets"]["Moon"]["nakshatra"]
        jup_t = transit["planets"]["Jupiter"]["sign"]
        sat_t = transit["planets"]["Saturn"]["sign"]
        
        active_factors = [
            f"Lagna: {asc} | Moon: {moon} ({nak})",
            f"Active Period: {active_dasha['mahadasha']} MD / {active_dasha['antardasha']} AD",
            f"Transits: Jupiter in {jup_t}, Saturn in {sat_t}",
            f"Key Yogas: {', '.join([y['name'] for y in yogas]) if yogas else 'Standard configurations'}"
        ]
        
        analysis = (
            f"With your {asc} Ascendant and Moon in {moon}, you are progressing through the {active_dasha['mahadasha']}-{active_dasha['antardasha']} Dasha timeline. "
            f"Transiting Jupiter in {jup_t} activates key growth sectors in your {req.category.lower()} sphere, creating fertile conditions for strategic expansion. "
            f"Saturn's presence in {sat_t} demands disciplined execution, foundational stability, and patience."
        )
        
        remedies = [
            f"Chant the seed mantra for {active_dasha['mahadasha']} regularly on its traditional ruler day.",
            "Practice mindful breathwork (Pranayama) every morning to harmonize mental clarity.",
            "Engage in intentional charity (daan) aligned with your active planetary rulers to smooth karmic currents."
        ]
        
        return AIAnswerResponse(
            question=req.question,
            category=req.category or "General Guidance",
            active_dasha={"mahadasha": active_dasha["mahadasha"], "antardasha": active_dasha["antardasha"]},
            astrological_factors=active_factors,
            analysis=analysis,
            practical_remedies=remedies
        )
