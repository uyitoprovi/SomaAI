"""Embeddings module."""

from typing import List


class EmbeddingModel:
    """Embedding model interface."""

    async def embed(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for texts."""
        pass
