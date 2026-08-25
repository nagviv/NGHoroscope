from fastapi import FastAPI, Depends, HTTPException, status, Response, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import asyncio
import json
from datetime import datetime, timezone

from app.db import engine, Base, get_db
from app.models.entities import User, SavedProfile
from app.core.auth import hash_password, verify_password, create_access_token, get_current_user
from app.models.requests import (
    BirthDetailsRequest, MatchMakingRequest, AIQuestionRequest, TransitRequest,
    UserRegisterRequest, UserLoginRequest, SaveProfileRequest, MuhurtaRequest, VarshaphalaRequest, ProgressionRequest
)
from app.models.responses import (
    NatalChartResponse, MatchMakingResponse, AIAnswerResponse, TransitResponse,
    PanchangResponse, JaiminiResponse, KPResponse, MuhurtaResponse, UserAuthResponse, ProfileResponse, KakshyaResponse, VarshaphalaResponse, SBCResponse, KotaResponse, ProgressionResponse
)
from app.services.chart_service import ChartService
from app.services.match_service import MatchService
from app.services.ai_service import AIService
from app.services.transit_service import TransitService
from app.services.panchang_service import PanchangService
from app.services.pdf_service import PDFService
from app.services.match_pdf_service import MatchPDFService
from app.services.jaimini_service import JaiminiService
from app.services.kp_service import KPService
from app.services.muhurta_service import MuhurtaService
from app.services.kakshya_service import KakshyaService
from app.services.varshaphala_service import VarshaphalaService
from app.services.payment_service import PaymentService
from app.core.sbc import calculate_sarvatobhadra_chakra
from app.core.kota import calculate_kota_chakra
from app.core.progressions import calculate_progressions
from app.core.ephemeris import compute_chart_raw

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Jyotish Platform Ultimate with Billing",
    description="Enterprise Astrological Engine with Stripe/Razorpay In-App Billing & WebSockets",
    version="18.0.0"
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
    return {"status": "healthy", "version": "18.0.0", "service": "jyotish-billing-suite"}

# BILLING & SUBSCRIPTIONS
@app.post("/api/v1/billing/checkout", tags=["Billing"])
def create_checkout(tier: str = "Premium_Monthly", user: User = Depends(get_current_user)):
    """Creates a checkout session for Stripe / Razorpay subscription."""
    return PaymentService.create_checkout_session(user, tier)

@app.post("/api/v1/billing/webhook", tags=["Billing"])
def payment_webhook(payload: dict, db: Session = Depends(get_db)):
    """Webhook handler for Stripe / Razorpay payment confirmations."""
    user_id = payload.get("user_id")
    tier = payload.get("tier", "Premium_Monthly")
    if user_id:
        PaymentService.fulfill_order(db, user_id, tier)
    return {"status": "processed"}

# WEBSOCKET REAL-TIME LIVE EPHEMERIS
@app.websocket("/ws/ephemeris/live")
async def websocket_ephemeris_live(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            now_dt = datetime.now(timezone.utc)
            live_chart = compute_chart_raw(now_dt, 5.5, 17.3850, 78.4867)
            payload = {"timestamp": now_dt.isoformat(), "ascendant": live_chart["ascendant"], "planets": live_chart["planets"]}
            await websocket.send_text(json.dumps(payload))
            await asyncio.sleep(1.0)
    except WebSocketDisconnect:
        pass

# AUTH & PROFILES
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

# ASTROLOGY CALCULATIONS
@app.post("/api/v1/chart/natal", response_model=NatalChartResponse, tags=["Charts"])
def create_natal_chart(payload: BirthDetailsRequest):
    return ChartService.generate_natal_chart(payload)

@app.post("/api/v1/chart/progressions", response_model=ProgressionResponse, tags=["Western Overlay"])
def get_secondary_progressions(payload: ProgressionRequest):
    b = payload.birth_details
    return calculate_progressions(datetime(b.year, b.month, b.day, b.hour, b.minute, b.second), payload.target_year, b.timezone_offset, b.latitude, b.longitude)

@app.post("/api/v1/chart/sbc", response_model=SBCResponse, tags=["Chakras"])
def get_sarvatobhadra_chakra(payload: TransitRequest):
    b = payload.birth_details
    return calculate_sarvatobhadra_chakra(datetime(b.year, b.month, b.day, b.hour, b.minute, b.second), datetime(payload.target_year, payload.target_month, payload.target_day, 12, 0, 0), b.timezone_offset, b.latitude, b.longitude)

@app.post("/api/v1/chart/kota", response_model=KotaResponse, tags=["Chakras"])
def get_kota_chakra(payload: TransitRequest):
    b = payload.birth_details
    return calculate_kota_chakra(datetime(b.year, b.month, b.day, b.hour, b.minute, b.second), datetime(payload.target_year, payload.target_month, payload.target_day, 12, 0, 0), b.timezone_offset, b.latitude, b.longitude)

@app.post("/api/v1/chart/varshaphala", response_model=VarshaphalaResponse, tags=["Varshaphala"])
def get_varshaphala_annual_chart(payload: VarshaphalaRequest):
    return VarshaphalaService.calculate_annual_chart(payload)

@app.post("/api/v1/chart/kakshya", response_model=KakshyaResponse, tags=["Ashtakavarga"])
def get_kakshya_transits(payload: TransitRequest):
    return KakshyaService.calculate_kakshya_system(payload)

@app.post("/api/v1/muhurta/calculate", response_model=MuhurtaResponse, tags=["Muhurta"])
def get_muhurta_analysis(payload: MuhurtaRequest):
    return MuhurtaService.calculate_muhurta_details(payload)

@app.post("/api/v1/chart/kp", response_model=KPResponse, tags=["KP Astrology"])
def get_kp_system(payload: BirthDetailsRequest):
    return KPService.calculate_kp_system(payload)

@app.post("/api/v1/chart/jaimini", response_model=JaiminiResponse, tags=["Jaimini"])
def get_jaimini_details(payload: BirthDetailsRequest):
    return JaiminiService.calculate_jaimini_system(payload)

@app.post("/api/v1/chart/pdf", tags=["Reports"])
def export_kundli_pdf(payload: BirthDetailsRequest):
    pdf_bytes = PDFService.generate_kundli_pdf(payload)
    return Response(content=pdf_bytes, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=kundli_report.pdf"})

@app.post("/api/v1/matchmaking/ashtakoota", response_model=MatchMakingResponse, tags=["Synastry"])
def compute_matchmaking(payload: MatchMakingRequest):
    return MatchService.calculate_compatibility(payload)

@app.post("/api/v1/matchmaking/pdf", tags=["Reports"])
def export_matchmaking_pdf(payload: MatchMakingRequest):
    pdf_bytes = MatchPDFService.generate_compatibility_pdf(payload)
    return Response(content=pdf_bytes, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=matchmaking_report.pdf"})

@app.post("/api/v1/chart/transits", response_model=TransitResponse, tags=["Transits"])
def get_current_transits(payload: TransitRequest):
    return TransitService.calculate_transits(payload)

@app.post("/api/v1/panchang/daily", response_model=PanchangResponse, tags=["Panchang"])
def get_daily_panchang(payload: BirthDetailsRequest):
    return PanchangService.calculate_panchang(payload)

@app.post("/api/v1/ai/ask", response_model=AIAnswerResponse, tags=["AI Astrologer"])
def ask_ai_astrologer(payload: AIQuestionRequest):
    return AIService.answer_question(payload)
