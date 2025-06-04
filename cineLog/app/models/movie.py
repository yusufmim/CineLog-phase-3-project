from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Movie(Base):
    __tablename__ = 'movies'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)