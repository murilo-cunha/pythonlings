# I AM NOT DONE

from fastapi import FastAPI, Depends, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()


def get_db():
    # Simulated database dependency
    return {"users": {"alice": {"name": "Alice", "role": "admin"}}}


@app.get("/users/{username}")
def get_user(username: str, db=Depends(get_db)):
    # Fix: look up username in db["users"], return the user dict
    # or raise HTTPException(status_code=404) if not found
    return {}


client = TestClient(app)


# DON'T EDIT THE TESTS
response = client.get("/users/alice")
assert response.status_code == 200
assert response.json()["name"] == "Alice"
assert response.json()["role"] == "admin"

response = client.get("/users/nobody")
assert response.status_code == 404
