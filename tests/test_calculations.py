from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_auth_and_profile_flow():
    reg_payload = {
        "name": "Tester",
        "email": "tester@test.com",
        "password": "Password123"
    }
    reg_res = client.post("/api/v1/auth/register", json=reg_payload)
    assert reg_res.status_code in [200, 400]
    
    login_res = client.post("/api/v1/auth/login", json={"email": "tester@test.com", "password": "Password123"})
    assert login_res.status_code == 200
    token = login_res.json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    prof_payload = {
        "name": "My Chart",
        "relationship_label": "Self",
        "year": 1995, "month": 8, "day": 15, "hour": 14, "minute": 30, "second": 0,
        "timezone_offset": 5.5, "latitude": 17.3850, "longitude": 78.4867, "location_name": "Hyderabad"
    }
    create_prof = client.post("/api/v1/profiles", json=prof_payload, headers=headers)
    assert create_prof.status_code == 200
    
    list_profs = client.get("/api/v1/profiles", headers=headers)
    assert list_profs.status_code == 200
    assert len(list_profs.json()) >= 1
