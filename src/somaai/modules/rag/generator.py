"""RAG generator."""
from typing import List


class BaseGenerator:
    """Abstract base class for RAG context-based generators."""

    async def generate(self, query: str, context: List[str]) -> str:
        """Generate a response based on the query and provided context."""
        pass


class AnalogyGenerator(BaseGenerator):
    """Generates explanations using analogies derived from the retrieved context."""

    async def generate(self, query: str, context: List[str]) -> str:
        pass


class RealWorldUseCaseGenerator(BaseGenerator):
    """Generates practical, real-world application scenarios based on the context."""

    async def generate(self, query: str, context: List[str]) -> str:
        pass


class CombinedGenerator(BaseGenerator):
    """Synthesizes multiple generation strategies into a comprehensive unified response."""

    async def generate(self, query: str, context: List[str]) -> str:
        pass

