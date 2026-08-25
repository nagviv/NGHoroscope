from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.requests import BirthDetailsRequest, MatchMakingRequest, AIQuestionRequest, TransitRequest
from app.models.responses import NatalChartResponse, MatchMakingResponse, AIAnswerResponse, TransitResponse, PanchangResponse
from app.services.chart_service import ChartService
from app.services.match_service import MatchService
from app.services.ai_service import AIService
from app.services.transit_service import TransitService
from app.services.panchang_service import PanchangService

app = FastAPI(
    title="Jyotish Engine & AI Astrologer API",
    description="High-precision Vedic Astrological Microservice with AI Q&A and Transit Analytics",
    version="3.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Status"])
def health_check():
    return {"status": "healthy", "version": "3.0.0", "service": "jyotish-core-ai"}

@app.post("/api/v1/chart/natal", response_model=NatalChartResponse, tags=["Charts"])
def create_natal_chart(payload: BirthDetailsRequest):
    """Calculates D1/D9/D10 charts, Vimshottari Dasha, Yogas, Doshas, and Ashtakavarga."""
    return ChartService.generate_natal_chart(payload)

@app.post("/api/v1/chart/transits", response_model=TransitResponse, tags=["Transits"])
def get_current_transits(payload: TransitRequest):
    """Computes current real-time planetary transits (Gochar) overlaid on natal houses."""
    return TransitService.calculate_transits(payload)

@app.post("/api/v1/panchang/daily", response_model=PanchangResponse, tags=["Panchang"])
def get_daily_panchang(payload: BirthDetailsRequest):
    """Computes Daily Vedic Panchang (Tithi, Vara, Nakshatra, Yoga, Karana, Rahu Kaal)."""
    return PanchangService.calculate_panchang(payload)

@app.post("/api/v1/matchmaking/ashtakoota", response_model=MatchMakingResponse, tags=["Synastry"])
def compute_matchmaking(payload: MatchMakingRequest):
    """Performs 36-point Ashtakoota compatibility analysis and Mangal Dosha cross-check."""
    return MatchService.calculate_compatibility(payload)

@app.post("/api/v1/ai/ask", response_model=AIAnswerResponse, tags=["AI Astrologer"])
def ask_ai_astrologer(payload: AIQuestionRequest):
    """Context-aware AI Astrologer: injects exact natal chart, dashas, transits, and yogas into the LLM prompt."""
    return AIService.answer_question(payload)
