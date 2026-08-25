from typing import Dict, List, Optional
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

class NatalChartResponse(BaseModel):
    ascendant: EntityPosition
    planets: Dict[str, PlanetPosition]
    vargas: Dict[str, Dict[str, str]]
    vimshottari_dasha: List[MahadashaItem]
