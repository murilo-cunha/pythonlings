"""
FastAPI uses Python type annotations to define path parameters and response types.
@app.get("/items/{item_id}") with def get_item(item_id: int) — FastAPI parses
and validates the path segment automatically, converting "42" → 42.

Complete get_item to return {"item_id": item_id, "name": f"Item {item_id}"}.
"""

# I AM NOT DONE

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {}


client = TestClient(app)
