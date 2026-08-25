from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.requests import BirthDetailsRequest
from app.models.responses import NatalChartResponse
from app.services.chart_service import ChartService

app = FastAPI(
    title="Jyotish Engine API",
    description="High-precision Vedic Astrological Calculation Microservice",
    version="1.0.0"
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
    return {"status": "healthy", "service": "jyotish-core"}

@app.post("/api/v1/chart/natal", response_model=NatalChartResponse, tags=["Calculations"])
def create_natal_chart(payload: BirthDetailsRequest):
    """Calculates D1 Rashi, D9 Navamsha, D10 Dashamsha, and Vimshottari Dasha."""
    return ChartService.generate_natal_chart(payload)
