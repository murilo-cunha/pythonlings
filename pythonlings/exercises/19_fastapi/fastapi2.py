# I AM NOT DONE

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.post("/items/", status_code=201)
def create_item(item: Item):
    # Fix: return {"id": 1, "name": item.name, "price": item.price}
    return {}


client = TestClient(app)


# DON'T EDIT THE TESTS
response = client.post("/items/", json={"name": "Widget", "price": 9.99})
assert response.status_code == 201
data = response.json()
assert data["id"] == 1
assert data["name"] == "Widget"
assert data["price"] == 9.99
