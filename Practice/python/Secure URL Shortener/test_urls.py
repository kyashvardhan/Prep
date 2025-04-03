from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_shorten_and_redirect():
    # Register a user
    client.post("/auth/register", data={"username": "test", "password": "123"})

    # Login
    res = client.post("/auth/token", data={"username": "test", "password": "123"})
    token = res.json()["access_token"]

    # Shorten URL
    headers = {"Authorization": f"Bearer {token}"}
    res = client.post("/shorten", params={"original": "https://example.com"}, headers=headers)
    assert res.status_code == 200
