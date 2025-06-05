# init_db.py
from app.database import engine
from app.models.journal_entry import JournalEntry
from app.models.user import User
from app.models.base import Base

Base.metadata.create_all(engine)
print("✅ Tables created successfully.")