from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_jaimini_endpoint():
    payload = {
        "year": 1995, "month": 8, "day": 15, "hour": 14, "minute": 30, "second": 0,
        "timezone_offset": 5.5, "latitude": 17.3850, "longitude": 78.4867
    }
    res = client.post("/api/v1/chart/jaimini", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "karakas" in data
    assert "atmakaraka_planet" in data
    assert "karakamsha_sign" in data
    assert "arudha_lagna" in data
    assert len(data["chara_dasha"]) == 12
