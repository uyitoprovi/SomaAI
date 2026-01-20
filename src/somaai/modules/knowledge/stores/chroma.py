"""Chroma vector store implementation."""

from typing import List

from somaai.modules.knowledge.vectorstore import VectorStore


class ChromaStore(VectorStore):
    """Chroma vector store."""

    async def add(self, texts: List[str], embeddings: List[List[float]]) -> None:
        """Add documents to Chroma."""
        pass

    async def search(self, embedding: List[float], top_k: int = 5) -> List[dict]:
        """Search Chroma for similar documents."""
        return []

    async def delete(self, ids: List[str]) -> None:
        """Delete documents from Chroma."""
        pass
