from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_stripe_billing_session():
    reg = client.post("/api/v1/auth/register", json={"name": "Test User", "email": "testuser@stripe.com", "password": "Password123"})
    token = client.post("/api/v1/auth/login", json={"email": "testuser@stripe.com", "password": "Password123"}).json()["access_token"]
    res = client.post("/api/v1/billing/checkout?tier=Premium_Monthly", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    assert "checkout_url" in res.json()
