from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_matchmaking_pdf():
    payload = {
        "bride": {
            "year": 1996, "month": 5, "day": 10, "hour": 10, "minute": 15, "second": 0,
            "timezone_offset": 5.5, "latitude": 28.6139, "longitude": 77.2090
        },
        "groom": {
            "year": 1994, "month": 11, "day": 20, "hour": 18, "minute": 45, "second": 0,
            "timezone_offset": 5.5, "latitude": 19.0760, "longitude": 72.8777
        }
    }
    res = client.post("/api/v1/matchmaking/pdf", json=payload)
    assert res.status_code == 200
    assert res.headers["content-type"] == "application/pdf"
    assert len(res.content) > 1000
