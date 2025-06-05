from sqlalchemy import Column, Integer, String, Date, Text, Boolean
from app.models.base import Base

class JournalEntry(Base):
    __tablename__ = 'journal_entries'
    id = Column(Integer, primary_key=True)
    movie_title = Column(String)
    date_watched = Column(Date)
    mood_before = Column(String)
    mood_after = Column(String)
    thoughts = Column(Text)
    rating = Column(Integer)
    mood_changed = Column(Boolean, default=False)  # ✅ Add this line

