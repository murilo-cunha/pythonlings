# I AM NOT DONE

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

ITEMS = [
    {"id": 1, "name": "Apple", "category": "fruit"},
    {"id": 2, "name": "Carrot", "category": "vegetable"},
    {"id": 3, "name": "Banana", "category": "fruit"},
]


@app.get("/items/")
def list_items(category: str = None):
    # Fix: if category is provided, filter ITEMS by category; otherwise return all
    return ITEMS  # Fix this


client = TestClient(app)


# DON'T EDIT THE TESTS
response = client.get("/items/")
assert response.status_code == 200
assert len(response.json()) == 3

response = client.get("/items/?category=fruit")
assert response.status_code == 200
fruits = response.json()
assert len(fruits) == 2
assert all(f["category"] == "fruit" for f in fruits)
