from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_kp_endpoint():
    payload = {
        "year": 1995, "month": 8, "day": 15, "hour": 14, "minute": 30, "second": 0,
        "timezone_offset": 5.5, "latitude": 17.3850, "longitude": 78.4867
    }
    res = client.post("/api/v1/chart/kp", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "cusps" in data
    assert len(data["cusps"]) == 12
    assert "planets" in data
    assert "ruling_planets" in data
    assert "sub_lord" in data["cusps"][0]
