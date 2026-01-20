"""Chat module schemas."""

from pydantic import BaseModel


class ChatMessage(BaseModel):
    """Chat message schema."""

    content: str


class ChatResponse(BaseModel):
    """Chat response schema."""

    response: str
