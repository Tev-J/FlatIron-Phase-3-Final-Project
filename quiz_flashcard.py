from .base import Base
from sqlalchemy import Column, Integer, Table, ForeignKey

quiz_flashcard = Table(
    "quiz_flashcard",
    Base.metadata,
    Column("quiz_id", Integer, ForeignKey("quiz.id"), primary_key=True),
    Column("flashcard_id", Integer, ForeignKey("flashcard.id"), primary_key=True),
)
