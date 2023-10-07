from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship


class Quiz(Base):
    __tablename__ = "quiz"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(55), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    user_id = Column(Integer, ForeignKey("user.id"), name="quiz_user", nullable=False)

    user = relationship("User", backref="quizzes")

    def __repr__(self):
        return (
            f"\ntitle = {self.title}"
            + f"\ncreated_at = {self.created_at} "
            + f"\nupdated_at = {self.updated_at} "
            + f"\nuser_id = {self.user_id} "
            + f"\nuser = {self.user} "
            + " >\n"
        )
