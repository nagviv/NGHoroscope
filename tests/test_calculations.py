from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_natal_chart_endpoint():
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
    
    # Assert primary structure
    assert "ascendant" in data
    assert "planets" in data
    assert "vargas" in data
    assert "vimshottari_dasha" in data
    
    # Check that all 9 grahas are present
    expected_grahas = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu"]
    for graha in expected_grahas:
        assert graha in data["planets"]
        assert "longitude" in data["planets"][graha]
        assert "house" in data["planets"][graha]
        assert "nakshatra" in data["planets"][graha]
        
    # Check Dasha structure
    assert len(data["vimshottari_dasha"]) == 9
    assert data["vimshottari_dasha"][0]["is_balance"] is True
