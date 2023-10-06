from .base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class UserResponse(Base):
    __tablename__ = "user_responses"

    id = Column(Integer, primary_key=True)
    flashcard_id = Column(Integer, ForeignKey("flashcard.id"))
    selected_answer = Column(String)
    is_correct = Column(Boolean)
    quiz_attempt_id = Column(Integer, ForeignKey("quiz_attempts.id"))