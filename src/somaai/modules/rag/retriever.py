"""RAG retriever."""

from typing import List


class Retriever:
    """Document retriever."""

    async def retrieve(self, query: str, top_k: int = 15) -> List[dict]:
        """Retrieve relevant documents."""
        return []
