from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_muhurta():
    payload = {"year": 2026, "month": 8, "day": 25, "latitude": 17.3850, "longitude": 78.4867}
    res = client.post("/api/v1/muhurta/calculate", json=payload)
    assert res.status_code == 200
    assert "choghadiya_day" in res.json()
