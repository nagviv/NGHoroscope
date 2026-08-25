from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_varshaphala():
    payload = {
        "birth_details": {
            "year": 1995, "month": 8, "day": 15, "hour": 14, "minute": 30, "second": 0,
            "timezone_offset": 5.5, "latitude": 17.3850, "longitude": 78.4867
        },
        "target_year": 2026
    }
    res = client.post("/api/v1/chart/varshaphala", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "muntha" in data
    assert "varsheshwara" in data
    assert "varsha_ascendant" in data
