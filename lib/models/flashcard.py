from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, func


class Flashcard(Base):
    __tablename__ = "flashcard"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String, nullable=False, unique=True)
    answer = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return (
            f"\nquestion = {self.question}"
            + f"\nanswer = {self.answer}"
            + f"\ncreated_at = {self.created_at}, "
            + f"\nupdated_at = {self.updated_at}, "
            + " >\n"
        )
