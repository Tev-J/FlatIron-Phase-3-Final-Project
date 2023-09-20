from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, func


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(55), nullable=False)
    password = Column(String(36), nullable=False)

    def __repr__(self):
        return (
            f"\n<User "
            + f"\nid = {self.id}, "
            + f"\nusername = {self.username}, "
            + "\n"
        )
