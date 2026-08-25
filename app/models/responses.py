from typing import Dict, List, Optional, Any
from pydantic import BaseModel

class EntityPosition(BaseModel):
    longitude: float
    sign: str
    sign_index: int
    degree_in_sign: float
    nakshatra: str
    pada: int
    d9_sign: str
    d10_sign: str

class PlanetPosition(EntityPosition):
    is_retrograde: bool
    speed: float
    house: int

class AntardashaItem(BaseModel):
    lord: str
    start_date: str
    end_date: str
    duration_months: float

class MahadashaItem(BaseModel):
    lord: str
    start_date: str
    end_date: str
    duration_years: float
    is_balance: bool
    antardashas: Optional[List[AntardashaItem]] = None

class YogaItem(BaseModel):
    name: str
    category: str
    description: str

class DoshaAnalysis(BaseModel):
    mangal_dosha: Dict[str, Any]
    sade_sati: Dict[str, Any]
    kaal_sarp: Dict[str, Any]

class NatalChartResponse(BaseModel):
    ascendant: EntityPosition
    planets: Dict[str, PlanetPosition]
    vargas: Dict[str, Dict[str, str]]
    vimshottari_dasha: List[MahadashaItem]
    yogas: List[YogaItem]
    doshas: DoshaAnalysis
    ashtakavarga: Dict[str, Any]
    shadbala: Dict[str, Any]

class MatchMakingResponse(BaseModel):
    ashtakoota: Dict[str, Any]
    bride_mangal_dosha: Dict[str, Any]
    groom_mangal_dosha: Dict[str, Any]
    overall_compatibility: str

class AIAnswerResponse(BaseModel):
    question: str
    category: str
    active_dasha: Dict[str, str]
    astrological_factors: List[str]
    analysis: str
    practical_remedies: List[str]

class TransitResponse(BaseModel):
    transit_date: str
    transit_planets: Dict[str, Dict[str, Any]]
    transits_from_lagna: Dict[str, int]
    transits_from_moon: Dict[str, int]
    sade_sati_status: Dict[str, Any]

class PanchangResponse(BaseModel):
    date: str
    tithi: Dict[str, Any]
    vara: str
    nakshatra: Dict[str, Any]
    yoga_index: int
    rahu_kaal: str
