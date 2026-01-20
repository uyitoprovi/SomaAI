"""Test configuration."""

import pytest
from fastapi.testclient import TestClient

from somaai.app import create_app


@pytest.fixture
def client():
    """Create test client."""
    app = create_app()
    with TestClient(app) as c:
        yield c
