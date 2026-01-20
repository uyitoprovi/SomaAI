"""Vector store interface."""

from abc import ABC, abstractmethod
from typing import List


class VectorStore(ABC):
    """Abstract vector store interface."""

    @abstractmethod
    async def add(self, texts: List[str], embeddings: List[List[float]]) -> None:
        """Add documents to the store."""
        pass

    @abstractmethod
    async def search(self, embedding: List[float], top_k: int = 5) -> List[dict]:
        """Search for similar documents."""
        pass

    @abstractmethod
    async def delete(self, ids: List[str]) -> None:
        """Delete documents from the store."""
        pass
