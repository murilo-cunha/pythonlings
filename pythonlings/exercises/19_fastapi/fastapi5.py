"""
FastAPI supports async route handlers with async def for non-blocking I/O.
TestClient (backed by httpx) handles async routes transparently in tests.
Use async def for I/O-bound work (database queries, HTTP calls);
sync def is fine for CPU-bound or in-memory work.

Complete the async compute endpoint to return {"n": n, "square": n**2, "cube": n**3}.
"""

# I AM NOT DONE

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/compute/{n}")
async def compute(n: int):
    return {}


client = TestClient(app)
