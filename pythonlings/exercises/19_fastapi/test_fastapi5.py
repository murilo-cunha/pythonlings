from fastapi5 import client


def test_compute_status():
    response = client.get("/compute/4")
    assert response.status_code == 200

def test_compute_values():
    data = client.get("/compute/4").json()
    assert data["n"] == 4
    assert data["square"] == 16
    assert data["cube"] == 64

def test_compute_different_n():
    data = client.get("/compute/3").json()
    assert data["square"] == 9
    assert data["cube"] == 27
