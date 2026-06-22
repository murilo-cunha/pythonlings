# I AM NOT DONE

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Fix: return {"item_id": item_id, "name": f"Item {item_id}"}
    return {}


client = TestClient(app)


# DON'T EDIT THE TESTS
response = client.get("/items/42")
assert response.status_code == 200
data = response.json()
assert data["item_id"] == 42
assert data["name"] == "Item 42"
