from app.models.user import User
from app.models.base import Base, engine, session

# Drop and recreate tables (optional)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Add sample users
users = [
    User(name="Alice", email="alice@example.com"),
    User(name="Bob", email="bob@example.com"),
    User(name="Charlie", email="charlie@example.com"),
]

session.add_all(users)
session.commit()

print("Database seeded with users!")
