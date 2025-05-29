from datetime import datetime
from sqlalchemy.orm import Session
from . import models

# USER CRUD
def create_user(db: Session, username: str):
    user = models.User(username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_all_users(db: Session):
    return db.query(models.User).all()

def delete_user(db: Session, user_id: int):
    user = db.get(models.User, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

# MOVIE NIGHT CRUD
def create_movie_night(db: Session, user_id: int, date: datetime.date, location: str):
    movie_night = models.MovieNight(date=date, location=location, user_id=user_id)
    db.add(movie_night)
    db.commit()
    db.refresh(movie_night)
    return movie_night

def get_movie_nights_by_user(db: Session, user_id: int):
    return db.query(models.MovieNight).filter(models.MovieNight.user_id == user_id).all()

def delete_movie_night(db: Session, movie_night_id: int):
    movie_night = db.get(models.MovieNight, movie_night_id)
    if movie_night:
        db.delete(movie_night)
        db.commit()
        return True
    return False

# MOVIE CRUD
def create_movie(db: Session, movie_night_id: int, title: str, genre: str = None, rating: int = None):
    movie = models.Movie(title=title, genre=genre, rating=rating, movie_night_id=movie_night_id)
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

def get_movies_by_movie_night(db: Session, movie_night_id: int):
    return db.query(models.Movie).filter(models.Movie.movie_night_id == movie_night_id).all()

def delete_movie(db: Session, movie_id: int):
    movie = db.get(models.Movie, movie_id)
    if movie:
        db.delete(movie)
        db.commit()
        return True
    return False
