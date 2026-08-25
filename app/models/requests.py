from pydantic import BaseModel, Field

class BirthDetailsRequest(BaseModel):
    year: int = Field(..., example=1995)
    month: int = Field(..., ge=1, le=12, example=8)
    day: int = Field(..., ge=1, le=31, example=15)
    hour: int = Field(..., ge=0, le=23, example=14)
    minute: int = Field(..., ge=0, le=59, example=30)
    second: int = Field(default=0, ge=0, le=59, example=0)
    timezone_offset: float = Field(..., example=5.5, description="UTC offset in hours, e.g., 5.5 for IST")
    latitude: float = Field(..., ge=-90.0, le=90.0, example=17.3850)
    longitude: float = Field(..., ge=-180.0, le=180.0, example=78.4867)


class MatchMakingRequest(BaseModel):
    bride: BirthDetailsRequest
    groom: BirthDetailsRequest
