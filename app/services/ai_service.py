from datetime import datetime
from app.models.requests import AIQuestionRequest
from app.models.responses import AIAnswerResponse

class AIService:
    @staticmethod
    def answer_question(req: AIQuestionRequest) -> AIAnswerResponse:
        return AIAnswerResponse(
            question=req.question, category=req.category or "General",
            active_dasha={"mahadasha": "Jupiter", "antardasha": "Saturn"},
            astrological_factors=["Lagna: Leo", "Active Dasha: Jupiter"],
            analysis="Favorable phase for career advancement.",
            practical_remedies=["Morning meditation"]
        )
