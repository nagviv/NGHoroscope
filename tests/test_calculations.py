from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_ai_ask_endpoint():
    payload = {
        "birth_details": {
            "year": 1995, "month": 8, "day": 15, "hour": 14, "minute": 30, "second": 0,
            "timezone_offset": 5.5, "latitude": 17.3850, "longitude": 78.4867
        },
        "question": "What does my current Dasha indicate for career advancement?",
        "category": "Career"
    }
    response = client.post("/api/v1/ai/ask", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "active_dasha" in data
    assert "analysis" in data
    assert len(data["practical_remedies"]) > 0
    assert "astrological_factors" in data

def test_transit_endpoint():
    payload = {
        "birth_details": {
            "year": 1995, "month": 8, "day": 15, "hour": 14, "minute": 30, "second": 0,
            "timezone_offset": 5.5, "latitude": 17.3850, "longitude": 78.4867
        },
        "target_year": 2026,
        "target_month": 8,
        "target_day": 25
    }
    response = client.post("/api/v1/chart/transits", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "transits_from_lagna" in data
    assert "transits_from_moon" in data

def test_panchang_endpoint():
    payload = {
        "year": 2026, "month": 8, "day": 25, "hour": 11, "minute": 0, "second": 0,
        "timezone_offset": 5.5, "latitude": 17.3850, "longitude": 78.4867
    }
    response = client.post("/api/v1/panchang/daily", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "tithi" in data
    assert "nakshatra" in data
    assert "rahu_kaal" in data
