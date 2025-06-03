from sqlalchemy import Column, Integer, String
from .base import Base

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)