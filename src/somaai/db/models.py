"""Database models."""

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from somaai.db.base import Base


class Document(Base):
    """Document model."""

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
