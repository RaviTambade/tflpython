from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all_policies():
    response = client.get("/api/policies/")

    assert response.status_code == 200
    assert len(response.json()) >= 3


def test_get_policy_by_id():
    response = client.get("/api/policies/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Jeevan Labh"


def test_get_policy_not_found():
    response = client.get("/api/policies/999")

    assert response.status_code == 404


def test_create_policy():
    policy = {
        "name": "Jeevan Secure",
        "description": "Secure life insurance plan",
        "maturity": "20 years",
        "premium": 25000
    }

    response = client.post("/api/policies/", json=policy)

    assert response.status_code == 200
    assert response.json()["name"] == "Jeevan Secure"


def test_update_policy():
    policy = {
        "name": "Updated Policy",
        "description": "Updated insurance plan",
        "maturity": "15 years",
        "premium": 30000
    }

    response = client.put("/api/policies/1", json=policy)

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Policy"


def test_delete_policy():
    response = client.delete("/api/policies/1")

    assert response.status_code == 200