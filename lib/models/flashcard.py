from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship


class Flashcard(Base):
    __tablename__ = "flashcard"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    user_id = Column(
        Integer, ForeignKey("user.id"), name="flashcard_user", nullable=False
    )
    user = relationship("User", backref="flashcards")
    categories = relationship("Category", backref="flashcards")

    def __repr__(self):
        return (
            f"\nquestion = {self.question}"
            + f"\nanswer = {self.answer}"
            + f"\ncreated_at = {self.created_at}, "
            + f"\nupdated_at = {self.updated_at}, "
            + " >\n"
        )
