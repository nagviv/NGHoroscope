from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_natal_chart_phase2():
    sample_payload = {
        "year": 1995,
        "month": 8,
        "day": 15,
        "hour": 14,
        "minute": 30,
        "second": 0,
        "timezone_offset": 5.5,
        "latitude": 17.3850,
        "longitude": 78.4867
    }
    
    response = client.post("/api/v1/chart/natal", json=sample_payload)
    assert response.status_code == 200
    data = response.json()
    
    # Assert Phase 2 expansions
    assert "yogas" in data
    assert "doshas" in data
    assert "ashtakavarga" in data
    assert "mangal_dosha" in data["doshas"]
    assert "sade_sati" in data["doshas"]
    assert "kaal_sarp" in data["doshas"]
    assert "sav_by_rashi" in data["ashtakavarga"]

def test_matchmaking_endpoint():
    match_payload = {
        "bride": {
            "year": 1996, "month": 5, "day": 10, "hour": 10, "minute": 15, "second": 0,
            "timezone_offset": 5.5, "latitude": 28.6139, "longitude": 77.2090
        },
        "groom": {
            "year": 1994, "month": 11, "day": 20, "hour": 18, "minute": 45, "second": 0,
            "timezone_offset": 5.5, "latitude": 19.0760, "longitude": 72.8777
        }
    }
    response = client.post("/api/v1/matchmaking/ashtakoota", json=match_payload)
    assert response.status_code == 200
    data = response.json()
    assert "ashtakoota" in data
    assert "total_score" in data["ashtakoota"]
    assert "bride_mangal_dosha" in data
    assert "groom_mangal_dosha" in data
