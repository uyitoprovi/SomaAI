"""Ingest endpoint.

ingest =  {upload, chunk, embed, store}

"""

from fastapi import APIRouter

router = APIRouter()


@router.post("/ingest")
async def ingest() -> dict:
    """Ingest documents."""
    return {"message": "Ingest endpoint"}
