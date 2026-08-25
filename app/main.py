from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from app.models.requests import BirthDetailsRequest, MatchMakingRequest, AIQuestionRequest, TransitRequest
from app.models.responses import NatalChartResponse, MatchMakingResponse, AIAnswerResponse, TransitResponse, PanchangResponse, JaiminiResponse
from app.services.chart_service import ChartService
from app.services.match_service import MatchService
from app.services.ai_service import AIService
from app.services.transit_service import TransitService
from app.services.panchang_service import PanchangService
from app.services.pdf_service import PDFService
from app.services.jaimini_service import JaiminiService

app = FastAPI(
    title="Jyotish Engine & Jaimini Sutras API",
    description="High-precision Vedic Astrological Microservice with Jaimini Chara Karakas and Chara Dasha",
    version="7.0.0"
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
    return {"status": "healthy", "version": "7.0.0", "service": "jyotish-jaimini-core"}

@app.post("/api/v1/chart/natal", response_model=NatalChartResponse, tags=["Charts"])
def create_natal_chart(payload: BirthDetailsRequest):
    return ChartService.generate_natal_chart(payload)

@app.post("/api/v1/chart/jaimini", response_model=JaiminiResponse, tags=["Jaimini Astrology"])
def get_jaimini_details(payload: BirthDetailsRequest):
    """Calculates Jaimini 7 Chara Karakas, Karakamsha, Arudha Lagna, and Chara Dasha."""
    return JaiminiService.calculate_jaimini_system(payload)

@app.post("/api/v1/chart/pdf", tags=["Reports"])
def export_kundli_pdf(payload: BirthDetailsRequest):
    pdf_bytes = PDFService.generate_kundli_pdf(payload)
    return Response(content=pdf_bytes, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=kundli_report.pdf"})

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
