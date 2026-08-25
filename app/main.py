from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from app.db import engine, Base, get_db
from app.models.entities import User, SavedProfile
from app.core.auth import hash_password, verify_password, create_access_token, get_current_user
from app.models.requests import (
    BirthDetailsRequest, MatchMakingRequest, AIQuestionRequest, TransitRequest,
    UserRegisterRequest, UserLoginRequest, SaveProfileRequest
)
from app.models.responses import (
    NatalChartResponse, MatchMakingResponse, AIAnswerResponse, TransitResponse,
    PanchangResponse, JaiminiResponse, UserAuthResponse, ProfileResponse
)
from app.services.chart_service import ChartService
from app.services.match_service import MatchService
from app.services.ai_service import AIService
from app.services.transit_service import TransitService
from app.services.panchang_service import PanchangService
from app.services.pdf_service import PDFService
from app.services.jaimini_service import JaiminiService

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Jyotish Engine, Jaimini & Auth API",
    description="High-precision Vedic Astrological Microservice with User Profiles and Authentication",
    version="8.0.0"
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
    return {"status": "healthy", "version": "8.0.0", "service": "jyotish-auth-core"}

# AUTH ENDPOINTS
@app.post("/api/v1/auth/register", response_model=UserAuthResponse, tags=["Auth"])
def register_user(payload: UserRegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=payload.email, hashed_password=hash_password(payload.password), name=payload.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    token = create_access_token({"sub": user.email, "id": user.id})
    return UserAuthResponse(access_token=token, token_type="bearer", name=user.name, email=user.email)

@app.post("/api/v1/auth/login", response_model=UserAuthResponse, tags=["Auth"])
def login_user(payload: UserLoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_access_token({"sub": user.email, "id": user.id})
    return UserAuthResponse(access_token=token, token_type="bearer", name=user.name, email=user.email)

# SAVED PROFILES
@app.get("/api/v1/profiles", response_model=List[ProfileResponse], tags=["Profiles"])
def list_profiles(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(SavedProfile).filter(SavedProfile.user_id == user.id).all()

@app.post("/api/v1/profiles", response_model=ProfileResponse, tags=["Profiles"])
def save_profile(payload: SaveProfileRequest, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    profile = SavedProfile(user_id=user.id, **payload.dict())
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

@app.delete("/api/v1/profiles/{profile_id}", tags=["Profiles"])
def delete_profile(profile_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    profile = db.query(SavedProfile).filter(SavedProfile.id == profile_id, SavedProfile.user_id == user.id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    db.delete(profile)
    db.commit()
    return {"message": "Profile deleted successfully"}

# ASTROLOGY CALCULATIONS
@app.post("/api/v1/chart/natal", response_model=NatalChartResponse, tags=["Charts"])
def create_natal_chart(payload: BirthDetailsRequest):
    return ChartService.generate_natal_chart(payload)

@app.post("/api/v1/chart/jaimini", response_model=JaiminiResponse, tags=["Jaimini"])
def get_jaimini_details(payload: BirthDetailsRequest):
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
