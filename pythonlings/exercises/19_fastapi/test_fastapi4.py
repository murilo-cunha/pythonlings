from fastapi4 import client


def test_get_existing_user():
    response = client.get("/users/alice")
    assert response.status_code == 200

def test_user_fields():
    data = client.get("/users/alice").json()
    assert data["name"] == "Alice"
    assert data["role"] == "admin"

def test_user_not_found():
    response = client.get("/users/nobody")
    assert response.status_code == 404
