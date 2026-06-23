from fastapi2 import client


def test_create_item_status():
    response = client.post("/items/", json={"name": "Widget", "price": 9.99})
    assert response.status_code == 201

def test_create_item_id():
    data = client.post("/items/", json={"name": "Widget", "price": 9.99}).json()
    assert data["id"] == 1

def test_create_item_fields():
    data = client.post("/items/", json={"name": "Gadget", "price": 4.99}).json()
    assert data["name"] == "Gadget"
    assert data["price"] == 4.99
