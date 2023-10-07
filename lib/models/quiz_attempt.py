from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    quiz_id = Column(Integer, ForeignKey("quiz.id"))
    start_time = Column(DateTime, default=func.now())
    end_time = Column(DateTime)
    score = Column(Integer)

    responses = relationship("UserResponse", backref="quiz_attempt")

    def __repr__(self):
        return (
            f"\nuser_id = {self.user_id}"
            + f"\nquiz_id = {self.quiz_id}"
            + f"\nstart_time = {self.start_time}, "
            + f"\nend_time = {self.end_time}, "
            + "\n"
        )
