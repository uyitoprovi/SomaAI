"""Admin endpoint."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/stats")
async def stats() -> dict:
    """Get system statistics."""
    return {"message": "Admin stats endpoint"}
