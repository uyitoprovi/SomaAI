"""Users module schemas."""

from pydantic import BaseModel


class User(BaseModel):
    """User schema."""

    id: str
    email: str
    name: str
