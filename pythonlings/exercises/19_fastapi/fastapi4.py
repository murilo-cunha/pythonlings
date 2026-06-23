"""
Depends() injects shared dependencies into route handlers.
FastAPI calls the dependency function and passes its return value to your handler.
Use dependencies for shared resources: database connections, authentication, config.

Complete get_user: look up username in db["users"]; return the user dict,
or raise HTTPException(status_code=404) if the user is not found.
"""

# I AM NOT DONE

from fastapi import FastAPI, Depends, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()


def get_db():
    return {"users": {"alice": {"name": "Alice", "role": "admin"}}}


@app.get("/users/{username}")
def get_user(username: str, db=Depends(get_db)):
    return {}


client = TestClient(app)
