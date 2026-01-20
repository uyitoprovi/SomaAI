"""Ingest module service."""


class IngestService:
    """Ingest service."""

    async def ingest_document(self, source: str) -> dict:
        """Ingest a document."""
        return {"status": "ingested", "source": source}
