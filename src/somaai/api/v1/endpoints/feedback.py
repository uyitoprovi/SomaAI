"""Feedback endpoint."""

from fastapi import APIRouter

router = APIRouter()


@router.post("/teacher")
async def feedback() -> dict:
    """Submit feedback."""
    return {"message": "Feedback endpoint"}
