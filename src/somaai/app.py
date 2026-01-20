"""FastAPI application factory."""

from fastapi import FastAPI

from somaai.api.router import api_router
from somaai.health import health_router
from somaai.middleware import setup_middleware
from somaai.settings import settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        debug=settings.debug,
    )

    setup_middleware(app)
    app.include_router(health_router)
    app.include_router(api_router, prefix="/api")

    return app
