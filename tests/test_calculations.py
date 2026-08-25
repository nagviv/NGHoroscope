from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_natal_chart():
    payload = {
        "year": 1995, "month": 8, "day": 15, "hour": 14, "minute": 30, "second": 0,
        "timezone_offset": 5.5, "latitude": 17.3850, "longitude": 78.4867
    }
    response = client.post("/api/v1/chart/natal", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "ascendant" in data
    assert "planets" in data
    assert "yogas" in data
    assert "doshas" in data
