from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, func


class Quiz(Base):
    __tablename__ = "quiz"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(55), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return (
            f"\ntitle = {self.title}"
            + f"\ncreated_at = {self.created_at} "
            + f"\nupdated_at = {self.updated_at} "
            + " >\n"
        )
