"""
Simple FastAPI server with status, greeting, and sum endpoints.
Used as the web-facing part of the app for testing/demo purposes.
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Simple FastAPI Server",
    description="A FastAPI server with status and greeting endpoints.",
    version="1.0.0",
)


@app.get("/status")
def get_status() -> dict:
    """Returns the server status."""
    return {"status": "OK"}


@app.get("/version")
def get_version() -> dict:
    """Returns the app version."""
    return {"version": "1.0.0"}


@app.get("/sayhi/{name}")
def say_hi(name: str) -> dict:
    """Greets the user by name."""
    return {"message": f"Hi, {name}!"}


class SumRequest(BaseModel):
    """Request body for the /sum endpoint."""
    a: int
    b: int


@app.post("/sum")
def sum_numbers(data: SumRequest) -> dict:
    """Returns the sum of two numbers."""
    return {"sum": data.a + data.b}
