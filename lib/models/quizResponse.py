from .base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class UserResponse(Base):
    __tablename__ = "user_responses"

    id = Column(Integer, primary_key=True)
    flashcard_id = Column(Integer, ForeignKey("flashcard.id"))
    selected_answer = Column(String)
    is_correct = Column(Boolean)
    quiz_attempt_id = Column(Integer, ForeignKey("quiz_attempt.id"))

    def __repr__(self):
        return (
            f"\nflashcard_id = {self.flashcard_id}"
            + f"\nselected_answer = {self.selected_answer} "
            + f"\Correct? = {self.is_correct} "
            + f"Quiz Attempted ID = {self.quiz_attempt_id} "
            + " >\n"
        )
