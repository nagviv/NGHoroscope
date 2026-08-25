from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.requests import BirthDetailsRequest, MatchMakingRequest
from app.models.responses import NatalChartResponse, MatchMakingResponse
from app.services.chart_service import ChartService
from app.services.match_service import MatchService

app = FastAPI(
    title="Jyotish Engine API",
    description="Vedic Astrological Calculation & Classical Rules Engine (Yogas, Doshas, Matchmaking)",
    version="2.0.0"
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
    return {"status": "healthy", "version": "2.0.0", "service": "jyotish-core"}

@app.post("/api/v1/chart/natal", response_model=NatalChartResponse, tags=["Astrological Charts"])
def create_natal_chart(payload: BirthDetailsRequest):
    """Calculates D1/D9/D10 charts, Vimshottari Dasha, Yogas, Doshas, and Ashtakavarga."""
    return ChartService.generate_natal_chart(payload)

@app.post("/api/v1/matchmaking/ashtakoota", response_model=MatchMakingResponse, tags=["Synastry"])
def compute_matchmaking(payload: MatchMakingRequest):
    """Performs 36-point Ashtakoota compatibility analysis and Mangal Dosha check for prospective partners."""
    return MatchService.calculate_compatibility(payload)
