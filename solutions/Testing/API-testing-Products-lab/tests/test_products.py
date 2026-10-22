import pytest
from fastapi.testclient import TestClient

from main import app, products

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_products():
    products.clear()
    yield
    products.clear()


def sample_product():
    return {
        "id": 1,
        "name": "Keyboard",
        "price": 1200.0,
        "quantity": 10
    }


# CREATE
def test_create_product():
    response = client.post("/api/products",json=sample_product() )

    assert response.status_code == 201
    assert response.json()["name"] == "Keyboard"


def test_create_duplicate_product():
    client.post("/api/products", json=sample_product())

    response = client.post("/api/products",json=sample_product())

    assert response.status_code == 409


# READ ALL
def test_get_all_products():
    client.post("/api/products", json=sample_product())

    response = client.get("/api/products")

    assert response.status_code == 200
    assert len(response.json()) == 1


# READ ONE
def test_get_product_by_id():
    client.post("/api/products", json=sample_product())

    response = client.get("/api/products/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_missing_product():
    response = client.get("/api/products/99")

    assert response.status_code == 404


# UPDATE
def test_update_product():
    client.post("/api/products", json=sample_product())

    updated = {
        "id": 1,
        "name": "Mechanical Keyboard",
        "price": 2500.0,
        "quantity": 5
    }

    response = client.put("/api/products/1",json=updated)

    assert response.status_code == 200
    assert response.json()["name"] == "Mechanical Keyboard"
    assert response.json()["price"] == 2500.0


def test_update_missing_product():
    response = client.put("/api/products/99",
        json={
            "id": 99,
            "name": "Mouse",
            "price": 500,
            "quantity": 10
        }
    )

    assert response.status_code == 404


def test_update_id_mismatch():
    client.post("/api/products", json=sample_product())

    response = client.put("/api/products/1",
        json={
            "id": 2,
            "name": "Mouse",
            "price": 500,
            "quantity": 10
        }
    )

    assert response.status_code == 400


# DELETE
def test_delete_product():
    client.post("/api/products", json=sample_product())

    response = client.delete("/api/products/1")

    assert response.status_code == 200
    assert client.get("/api/products/1").status_code == 404


def test_delete_missing_product():
    response = client.delete("/api/products/99")

    assert response.status_code == 404


# VALIDATION
def test_invalid_product_price():
    invalid_product = {
        "id": 2,
        "name": "Mouse",
        "price": -10,
        "quantity": 5
    }

    response = client.post("/api/products",json=invalid_product)

    assert response.status_code == 422