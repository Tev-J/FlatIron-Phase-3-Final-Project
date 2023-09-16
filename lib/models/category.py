from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, func


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def __repr__(self):
        return f"\nname = {self.name}" + " >\n"
