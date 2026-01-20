"""API v1 router."""

from fastapi import APIRouter

from somaai.api.v1.endpoints import admin, chat, feedback, ingest, retrieval

v1_router = APIRouter()

# TODO:
# Remove some routes
# Add some routes

v1_router.include_router(chat.router, prefix="/chat", tags=["chat"])
v1_router.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
v1_router.include_router(retrieval.router, prefix="/retrieval", tags=["retrieval"])
v1_router.include_router(feedback.router, prefix="/feedback", tags=["feedback"])
v1_router.include_router(admin.router, prefix="/admin", tags=["admin"])
