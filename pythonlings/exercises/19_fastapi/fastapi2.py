"""
Declare a Pydantic BaseModel as a function parameter to accept a JSON request body.
FastAPI validates the incoming JSON against the model schema and raises 422 if invalid.
Use status_code= on the decorator to change the default 200 response code.

Complete create_item to return {"id": 1, "name": item.name, "price": item.price}.
"""

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
    return {}


client = TestClient(app)
