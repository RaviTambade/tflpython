import pytest
from fastapi.testclient import TestClient

from main import create_app


@pytest.fixture
def client():
    with TestClient(create_app()) as test_client:
        yield test_client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "application": "TFLInsurance",
        "message": "Welcome to TFLInsurance REST API",
        "docs": "/docs",
    }


def test_get_all_policies(client):
    response = client.get("/api/policies")

    assert response.status_code == 200
    assert response.json()["message"] == "Policies retrieved successfully"
    assert response.json()["count"] == 3
    assert len(response.json()["data"]) == 3


def test_get_policy_by_id(client):
    response = client.get("/api/policies/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Jeevan Labh"
    assert response.json()["premium"] == 15000.0


def test_get_policy_not_found(client):
    response = client.get("/api/policies/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Policy not found"


def test_create_policy(client):
    response = client.post(
        "/api/policies",
        json={
            "name": "Jeevan Anand",
            "description": "Life insurance protection plan",
            "maturity": "20 years",
            "premium": 18000.0,
        },
    )

    assert response.status_code == 201
    assert response.json()["message"] == "Policy created successfully"
    assert response.json()["data"]["id"] == 4
    assert response.json()["data"]["name"] == "Jeevan Anand"
    assert response.json()["data"]["premium"] == 18000.0


@pytest.mark.parametrize(
    "invalid_policy",
    [
        {
            "name": "Jeevan Anand",
            "description": "Life insurance protection plan",
            "maturity": "20 years",
        },
        {
            "name": "Jeevan Anand",
            "description": "Life insurance protection plan",
            "maturity": "20 years",
            "premium": -1,
        },
    ],
)
def test_create_policy_with_invalid_data(client, invalid_policy):
    response = client.post("/api/policies", json=invalid_policy)

    assert response.status_code == 422


def test_update_policy(client):
    response = client.put(
        "/api/policies/1",
        json={
            "name": "Jeevan Labh Updated",
            "description": "Updated life insurance plan",
            "maturity": "12 years",
            "premium": 17000.0,
        },
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Policy updated successfully"
    assert response.json()["data"]["id"] == 1
    assert response.json()["data"]["name"] == "Jeevan Labh Updated"
    assert response.json()["data"]["premium"] == 17000.0


def test_update_policy_not_found(client):
    response = client.put(
        "/api/policies/999",
        json={
            "name": "Unknown Policy",
            "description": "Test description",
            "maturity": "5 years",
            "premium": 10000.0,
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Policy not found"


def test_delete_policy(client):
    response = client.delete("/api/policies/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Policy deleted successfully"
    assert response.json()["deleted_policy"]["id"] == 1
    assert client.get("/api/policies/1").status_code == 404


def test_delete_policy_not_found(client):
    response = client.delete("/api/policies/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Policy not found"


def test_invalid_policy_id(client):
    response = client.get("/api/policies/abc")

    assert response.status_code == 422


def test_policy_data_is_isolated_between_clients():
    with TestClient(create_app()) as first_client:
        assert first_client.delete("/api/policies/1").status_code == 200

    with TestClient(create_app()) as second_client:
        assert second_client.get("/api/policies/1").status_code == 404
