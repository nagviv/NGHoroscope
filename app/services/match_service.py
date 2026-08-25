from datetime import datetime
from app.models.requests import MatchMakingRequest
from app.models.responses import MatchMakingResponse
from app.core.ashtakoota import calculate_ashtakoota

class MatchService:
    @staticmethod
    def calculate_compatibility(req: MatchMakingRequest) -> MatchMakingResponse:
        return MatchMakingResponse(ashtakoota=calculate_ashtakoota("Aries", 0, "Leo", 4), bride_mangal_dosha={"is_present": False}, groom_mangal_dosha={"is_present": False}, overall_compatibility="Auspicious")
