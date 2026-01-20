"""Ingest module schemas."""

from pydantic import BaseModel


class IngestRequest(BaseModel):
    """Ingest request schema."""

    source: str


class IngestResponse(BaseModel):
    """Ingest response schema."""

    status: str
    document_id: str
