from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_admin_stats():
    res = client.get("/api/v1/admin/stats")
    assert res.status_code == 200
    assert "active_calculations_per_sec" in res.json()
