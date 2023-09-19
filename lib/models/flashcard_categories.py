from .base import Base
from sqlalchemy import create_engine, Column, Integer, ForeignKey, Table


flashcard_categories = Table(
    "flashcard_categories",
    Base.metadata,
    Column("flashcard_id", Integer, ForeignKey("flashcard.id"), primary_key=True),
    Column("category_id", Integer, ForeignKey("category.id"), primary_key=True),
)
