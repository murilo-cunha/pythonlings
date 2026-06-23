"""
Query parameters are function parameters not included in the path pattern.
def list_items(category: str = None) captures GET /items/?category=fruit.
Optional params use None as the default; required params have no default.

Complete list_items: return all items, or only those matching category if provided.
"""

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
    return ITEMS


client = TestClient(app)
