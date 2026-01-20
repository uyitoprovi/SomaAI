"""Search endpoint.

search from the vector store
"""

from fastapi import APIRouter

router = APIRouter()


@router.post("/retrieval")
async def retrieval() -> dict:
    """Search knowledge base."""
    return {"message": "Search endpoint"}
