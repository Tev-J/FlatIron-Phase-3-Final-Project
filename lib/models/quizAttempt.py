from .base import Base
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship


class QuizAttempt(Base):
    __tablename__ = "quiz_attempt"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    quiz_id = Column(Integer, ForeignKey("quiz.id"))
    start_time = Column(DateTime, default=func.now())
    end_time = Column(DateTime)
    score = Column(Float, default=0.0)

    responses = relationship("QuizResponse", backref="quiz_attempt")

    def calculate_score(self):
        correct_responses = [
            response for response in self.responses if response.is_correct
        ]
        if self.responses:
            return len(correct_responses) / len(self.responses)
        return 0

    def __repr__(self):
        return (
            f"\nuser_id = {self.user_id}"
            + f"\nquiz_id = {self.quiz_id}"
            + f"\nstart_time = {self.start_time}, "
            + f"\nend_time = {self.end_time}, "
            + f"\# of correct answers = {self.score}, "
            + "\n"
        )
