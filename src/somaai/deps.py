"""Dependency injection."""

from typing import Generator


def get_db() -> Generator:
    """Get database session."""
    # Database session logic here
    yield None
