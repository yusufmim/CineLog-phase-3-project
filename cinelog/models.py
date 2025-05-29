from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)

    movie_nights = relationship("MovieNight", back_populates="user", cascade="all, delete-orphan")

class MovieNight(Base):
    __tablename__ = "movie_nights"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="movie_nights")
    movies = relationship("Movie", back_populates="movie_night", cascade="all, delete-orphan")

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=True)
    rating = Column(Integer, nullable=True)  # rating out of 10
    movie_night_id = Column(Integer, ForeignKey("movie_nights.id"))

    movie_night = relationship("MovieNight", back_populates="movies")
