import os
import json
from datetime import datetime, timezone
from app.models.requests import AIQuestionRequest
from app.models.responses import AIAnswerResponse
from app.core.ephemeris import compute_chart_raw
from app.core.dasha import calculate_vimshottari, get_active_dasha
from app.core.yogas import detect_yogas
from app.core.doshas import check_mangal_dosha, check_sade_sati

class AIService:
    @staticmethod
    def build_astrological_prompt_context(req: AIQuestionRequest) -> dict:
        birth_dt = datetime(req.birth_details.year, req.birth_details.month, req.birth_details.day,
                            req.birth_details.hour, req.birth_details.minute, req.birth_details.second)
        natal = compute_chart_raw(birth_dt, req.birth_details.timezone_offset, req.birth_details.latitude, req.birth_details.longitude)
        dasha_tree = calculate_vimshottari(natal["planets"]["Moon"]["longitude"], birth_dt)
        
        # Determine active dasha at current time
        now_dt = datetime.now(timezone.utc)
        active_dasha = get_active_dasha(dasha_tree, now_dt)
        yogas = detect_yogas(natal)
        
        # Calculate current real-time transits
        transit = compute_chart_raw(now_dt, req.birth_details.timezone_offset, req.birth_details.latitude, req.birth_details.longitude)
        saturn_transit_idx = transit["planets"]["Saturn"]["sign_index"]
        jup_transit_idx = transit["planets"]["Jupiter"]["sign_index"]
        sade_sati = check_sade_sati(natal["planets"]["Moon"]["sign_index"], saturn_transit_idx)
        
        return {
            "natal_ascendant": natal["ascendant"]["sign"],
            "natal_moon_sign": natal["planets"]["Moon"]["sign"],
            "natal_moon_nakshatra": natal["planets"]["Moon"]["nakshatra"],
            "tenth_house_lord_sign": natal["planets"].get("Sun", {}).get("sign"), # Baseline sample
            "active_mahadasha": active_dasha["mahadasha"],
            "active_antardasha": active_dasha["antardasha"],
            "active_yogas": [y["name"] for y in yogas],
            "transit_saturn_sign": transit["planets"]["Saturn"]["sign"],
            "transit_jupiter_sign": transit["planets"]["Jupiter"]["sign"],
            "sade_sati_status": sade_sati.get("phase", "None")
        }

    @staticmethod
    def answer_question(req: AIQuestionRequest) -> AIAnswerResponse:
        ctx = AIService.build_astrological_prompt_context(req)
        
        # Deterministic domain synthesis engine (can connect to OpenAI/Gemini/Anthropic via API key)
        active_factors = [
            f"Lagna: {ctx['natal_ascendant']} with Moon in {ctx['natal_moon_sign']} ({ctx['natal_moon_nakshatra']})",
            f"Active Period: {ctx['active_mahadasha']} Mahadasha / {ctx['active_antardasha']} Antardasha",
            f"Current Transits: Jupiter in {ctx['transit_jupiter_sign']}, Saturn in {ctx['transit_saturn_sign']} (Sade Sati: {ctx['sade_sati_status']})",
            f"Key Yogas: {', '.join(ctx['active_yogas']) if ctx['active_yogas'] else 'Standard planetary configurations'}"
        ]
        
        # Formulate grounded, constructive astrological synthesis
        analysis = (
            f"Based on your {ctx['natal_ascendant']} Ascendant and Moon in {ctx['natal_moon_sign']}, "
            f"you are currently running the {ctx['active_mahadasha']}-{ctx['active_antardasha']} Dasha cycle. "
            f"With Jupiter actively transiting {ctx['transit_jupiter_sign']}, this phase strongly activates growth, "
            f"discernment, and expanding opportunities in your {req.category.lower()} sphere. "
            f"Saturn's placement in {ctx['transit_saturn_sign']} emphasizes structured discipline, long-term foundation building, "
            f"and patient execution rather than hasty transitions."
        )
        
        remedies = [
            f"Chant the seed mantra for {ctx['active_mahadasha']} ({'Om Sham Shanaicharaya Namah' if ctx['active_mahadasha'] == 'Saturn' else 'Om Brihaspataye Namah' if ctx['active_mahadasha'] == 'Jupiter' else 'Om Namah Shivaya'}) on weekly ruler days.",
            "Engage in structured morning mindfulness and conscious breathwork to harmonize nervous energy.",
            "Practice purposeful charity (daan) aligned with your active Dasha lord to balance planetary karmic currents."
        ]
        
        return AIAnswerResponse(
            question=req.question,
            category=req.category or "General Guidance",
            active_dasha={"mahadasha": ctx["active_mahadasha"], "antardasha": ctx["active_antardasha"]},
            astrological_factors=active_factors,
            analysis=analysis,
            practical_remedies=remedies
        )
