from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base

class Review(Base):
    __tablename__ = 'reviews'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))