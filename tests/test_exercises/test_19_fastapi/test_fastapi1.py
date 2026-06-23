from fastapi1 import client


def test_get_item_status():
    response = client.get("/items/42")
    assert response.status_code == 200

def test_item_id():
    data = client.get("/items/42").json()
    assert data["item_id"] == 42

def test_item_name():
    data = client.get("/items/7").json()
    assert data["name"] == "Item 7"
