from datetime import datetime
from app.models.requests import AIQuestionRequest
from app.models.responses import AIAnswerResponse
from app.core.ephemeris import compute_chart_raw
from app.core.dasha import calculate_vimshottari, get_active_dasha

class AIService:
    @staticmethod
    def answer_question(req: AIQuestionRequest) -> AIAnswerResponse:
        b = req.birth_details
        birth_dt = datetime(b.year, b.month, b.day, b.hour, b.minute, b.second)
        raw = compute_chart_raw(birth_dt, b.timezone_offset, b.latitude, b.longitude)
        dasha_tree = calculate_vimshottari(raw["planets"]["Moon"]["longitude"], birth_dt)
        active_dasha = get_active_dasha(dasha_tree, datetime.utcnow())

        lagna = raw["ascendant"]
        planets = raw["planets"]
        q = req.question.lower()

        # Map houses and planetary significators dynamically based on keywords in the question
        if any(w in q for w in ["job", "career", "work", "profession", "business", "promotion", "boss"]):
            category = "Career & Profession"
            house_num = 10
            key_planets = ["Sun", "Saturn", "Mercury", "Jupiter"]
            focus_desc = "10th house of profession, career stability, and leadership potential."
        elif any(w in q for w in ["house", "property", "home", "land", "vehicle", "buy"]):
            category = "Real Estate & Assets"
            house_num = 4
            key_planets = ["Mars", "Venus", "Moon"]
            focus_desc = "4th house of immovable property, vehicles, domestic peace, and real estate acquisition."
        elif any(w in q for w in ["money", "wealth", "financial", "income", "gain", "rich", "save"]):
            category = "Wealth & Finance"
            house_num = 11
            key_planets = ["Jupiter", "Venus", "Mercury"]
            focus_desc = "2nd house (accumulated wealth) and 11th house (gains and financial inflow)."
        elif any(w in q for w in ["marriage", "love", "spouse", "partner", "relationship", "wedding"]):
            category = "Relationships & Marriage"
            house_num = 7
            key_planets = ["Venus", "Jupiter"]
            focus_desc = "7th house of partnerships, marriage harmony, and significant relationships."
        elif any(w in q for w in ["long", "duration", "life", "health", "future", "span", "age"]):
            category = "Longevity & General Life Path"
            house_num = 1
            key_planets = ["Saturn", "Sun", "Moon"]
            focus_desc = "1st house (Lagna/Self vitality) and 8th house (longevity and life path stability)."
        else:
            category = "General Astrological Inquiry"
            house_num = 1
            key_planets = ["Jupiter", "Sun", "Moon"]
            focus_desc = "Overall chart vitality, ascendant strength, and active planetary periods."

        # Find planets influencing the target house or active dasha lord
        influencing_planets = [
            pname for pname, pdata in planets.items() 
            if pdata.get("house") == house_num or pname in key_planets
        ]

        dasha_lord = active_dasha.get("mahadasha", "Current")
        antardasha_lord = active_dasha.get("antardasha", "")
        lagna_sign = lagna.get("sign", "Aries")
        moon_sign = planets.get("Moon", {}).get("sign", "Aries")

        # Dynamic synthesis based on actual chart data
        analysis = (
            f"Dynamic Astrological Evaluation for '{req.question}': "
            f"Your chart features a {lagna_sign} Ascendant with your Moon placed in {moon_sign}. "
            f"Evaluating this query through the lens of the {focus_desc}, your active {dasha_lord}-{antardasha_lord} dasha sequence "
            f"plays a vital role. Key planetary forces involving {', '.join(influencing_planets[:3])} indicate active shifts in this domain. "
            f"The alignment suggests that structured persistence, favorable planetary transits over your natal placements, and alignment with your "
            f"dasha timeline will yield positive outcomes for your inquiry."
        )

        remedies = [
            f"Focus constructive efforts and planning during favorable planetary hours governed by {dasha_lord}.",
            "Maintain consistency and mindful discipline regarding your goals.",
            "Strengthen core planetary energies through appropriate meditative practices or charity."
        ]

        return AIAnswerResponse(
            question=req.question,
            category=category,
            active_dasha=active_dasha,
            astrological_factors=[
                f"Lagna: {lagna_sign} ({lagna.get('degree', 0)}°)",
                f"Moon Sign: {moon_sign}",
                f"Active Dasha: {dasha_lord} / {antardasha_lord}",
                f"Primary Focus House: House #{house_num}"
            ],
            analysis=analysis,
            practical_remedies=remedies
        )