from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))