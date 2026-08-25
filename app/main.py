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
    version="5.0.0"
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
    return {"status": "healthy", "version": "5.0.0", "service": "jyotish-core-ai"}

@app.post("/api/v1/chart/natal", response_model=NatalChartResponse, tags=["Charts"])
def create_natal_chart(payload: BirthDetailsRequest):
    return ChartService.generate_natal_chart(payload)

@app.post("/api/v1/chart/transits", response_model=TransitResponse, tags=["Transits"])
def get_current_transits(payload: TransitRequest):
    return TransitService.calculate_transits(payload)

@app.post("/api/v1/panchang/daily", response_model=PanchangResponse, tags=["Panchang"])
def get_daily_panchang(payload: BirthDetailsRequest):
    return PanchangService.calculate_panchang(payload)

@app.post("/api/v1/matchmaking/ashtakoota", response_model=MatchMakingResponse, tags=["Synastry"])
def compute_matchmaking(payload: MatchMakingRequest):
    return MatchService.calculate_compatibility(payload)

@app.post("/api/v1/ai/ask", response_model=AIAnswerResponse, tags=["AI Astrologer"])
def ask_ai_astrologer(payload: AIQuestionRequest):
    return AIService.answer_question(payload)
