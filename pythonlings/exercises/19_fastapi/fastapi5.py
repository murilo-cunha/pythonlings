# I AM NOT DONE

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/compute/{n}")
async def compute(n: int):
    # Fix: return {"n": n, "square": n**2, "cube": n**3}
    return {}


client = TestClient(app)


# DON'T EDIT THE TESTS
response = client.get("/compute/4")
assert response.status_code == 200
data = response.json()
assert data["n"] == 4
assert data["square"] == 16
assert data["cube"] == 64
