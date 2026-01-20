"""Ingest pipeline."""


class IngestPipeline:
    """Document ingestion pipeline."""

    def __init__(self) -> None:
        """Initialize pipeline."""
        pass

    async def run(self, document: str) -> dict:
        """Run the ingestion pipeline."""
        return {"status": "completed"}
