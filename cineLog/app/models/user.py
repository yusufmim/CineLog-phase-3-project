from sqlalchemy import Column, Integer, String
from app.models.base import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)