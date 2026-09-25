from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Employee Management API is running"
    }


def test_create_employee_validation():
    response = client.post(
        "/employees/",
        json={
            "name": "A",
            "email": "wrong-email",
            "department": "I",
            "salary": -100
        }
    )

    assert response.status_code == 422