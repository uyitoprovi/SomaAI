"""RAG evaluation."""


class RAGEvaluator:
    """RAG evaluation utilities."""

    def evaluate_response(self, query: str, response: str, context: str) -> dict:
        """Evaluate a RAG response."""
        return {"relevance": 0.0, "faithfulness": 0.0}
