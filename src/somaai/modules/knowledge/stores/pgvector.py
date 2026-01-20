"""PGVector store implementation."""

from typing import List

from somaai.modules.knowledge.vectorstore import VectorStore


class PGVectorStore(VectorStore):
    """PGVector store."""

    async def add(self, texts: List[str], embeddings: List[List[float]]) -> None:
        """Add documents to PGVector."""
        pass

    async def search(self, embedding: List[float], top_k: int = 5) -> List[dict]:
        """Search PGVector for similar documents."""
        return []

    async def delete(self, ids: List[str]) -> None:
        """Delete documents from PGVector."""
        pass
