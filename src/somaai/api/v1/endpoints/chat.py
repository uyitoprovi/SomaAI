"""Chat endpoint."""

from fastapi import APIRouter

router = APIRouter()


@router.post("/student")
async def chat() -> dict:
    """Handle chat messages."""
    return {"message": "Chat endpoint"}

@router.post("/teacher")
async def chat() -> dict:
    """Handle chat messages."""
    return {"message": "Chat endpoint"}
