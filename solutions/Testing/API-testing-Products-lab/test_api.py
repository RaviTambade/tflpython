from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_existing_student():
    response = client.get("/api/students/101")

    assert response.status_code == 200
    assert response.json() == {
        "id": 101,
        "name": "Rahul",
    }


def test_get_missing_student():
    response = client.get("/api/students/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"