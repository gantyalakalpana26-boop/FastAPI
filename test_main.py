from fastapi.testclient import TestClient
from main import app, students

client = TestClient(app)


def setup_function():
    students.clear()


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_add_student():
    response = client.post(
        "/students",
        json={
            "name": "KALPANA",
            "roll_no": "MCA023",
            "marks": 82,
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "KALPANA"


def test_invalid_marks():
    response = client.post(
        "/students",
        json={
            "name": "Sneha",
            "roll_no": "MCA52",
            "marks": 85,
        },
    )

    assert response.status_code == 422