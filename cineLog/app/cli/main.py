from tabulate import tabulate
from app.models.user import User
from app.models.base import session
from app.models.journal_entry import JournalEntry
from datetime import datetime
from sqlalchemy import func

# --- User Functions ---

def view_users():
    users = session.query(User).all()
    if users:
        print(tabulate([[u.id, u.name, u.email] for u in users], headers=["ID", "Name", "Email"]))
    else:
        print("No users found.")

def add_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    new_user = User(name=name, email=email)
    session.add(new_user)
    session.commit()
    print(f"User {name} added.")

def delete_user():
    view_users()
    try:
        user_id = int(input("Enter ID of the user to delete: "))
        user = session.query(User).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            print(f"User ID {user_id} deleted.")
        else:
            print("User not found.")
    except ValueError:
        print("Invalid ID.")

def update_user():
    view_users()
    try:
        user_id = int(input("Enter ID of the user to update: "))
        user = session.query(User).get(user_id)
        if user:
            user.name = input(f"Enter new name (current: {user.name}): ") or user.name
            user.email = input(f"Enter new email (current: {user.email}): ") or user.email
            session.commit()
            print("User updated.")
        else:
            print("User not found.")
    except ValueError:
        print("Invalid input.")

# --- Journal Entry Functions ---

def add_journal_entry():
    title = input("Movie title: ")
    date_str = input("Date watched (YYYY-MM-DD): ")
    try:
        date_watched = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return
    mood_before = input("Mood before watching: ")
    mood_after = input("Mood after watching: ")
    thoughts = input("Personal thoughts/life lesson: ")
    rating = input("Rating out of 10 (optional): ")
    rating = int(rating) if rating.isdigit() else None

    mood_changed = mood_before.strip().lower() != mood_after.strip().lower()

    entry = JournalEntry(
        movie_title=title,
        date_watched=date_watched,
        mood_before=mood_before,
        mood_after=mood_after,
        thoughts=thoughts,
        rating=rating,
        mood_changed=mood_changed
    )
    session.add(entry)
    session.commit()

    print("\nJournal entry saved.")
    if mood_changed:
        print("✅ Mood changed!")
        show_top_mood_changers(title)
    else:
        print("🟡 No mood change recorded.")

def show_top_mood_changers(current_title):
    mood_changers = (
        session.query(JournalEntry.movie_title, func.count(JournalEntry.id).label("count"))
        .filter(JournalEntry.mood_changed == True)
        .group_by(JournalEntry.movie_title)
        .order_by(func.count(JournalEntry.id).desc())
        .limit(3)
        .all()
    )

    print("\n🎬 Top 3 Mood-Changing Movies:")
    for i, (title, count) in enumerate(mood_changers, start=1):
        tag = "🌟" if title == current_title else ""
        print(f"{i}. {title} ({count} mood changes) {tag}")

def view_all_entries():
    entries = session.query(JournalEntry).order_by(JournalEntry.date_watched.desc()).all()
    if not entries:
        print("No journal entries yet.")
        return

    for entry in entries:
        print(f"\n📘 ID: {entry.id}")
        print(f"🎬 {entry.movie_title} ({entry.date_watched})")
        print(f"🌀 Mood: {entry.mood_before} ➜ {entry.mood_after}")
        print(f"📝 Thoughts: {entry.thoughts}")
        print(f"⭐ Rating: {entry.rating}/10" if entry.rating is not None else "")
        print("-" * 40)

def delete_entry():
    view_all_entries()
    try:
        entry_id = int(input("Enter ID of the entry to delete: "))
        entry = session.query(JournalEntry).get(entry_id)
        if entry:
            session.delete(entry)
            session.commit()
            print("Entry deleted.")
        else:
            print("Entry not found.")
    except ValueError:
        print("Invalid ID.")

def search_entries():
    search_term = input("Enter movie title to search: ").strip()
    results = (
        session.query(JournalEntry)
        .filter(JournalEntry.movie_title.ilike(f"%{search_term}%"))
        .order_by(JournalEntry.date_watched.desc())
        .all()
    )

    if results:
        print(f"\n🔍 Results for '{search_term}':")
        for entry in results:
            print(f"\n📘 ID: {entry.id}")
            print(f"🎬 {entry.movie_title} ({entry.date_watched})")
            print(f"🌀 Mood: {entry.mood_before} ➜ {entry.mood_after}")
            print(f"📝 Thoughts: {entry.thoughts}")
            print(f"⭐ Rating: {entry.rating}/10" if entry.rating is not None else "")
            print("-" * 40)
    else:
        print("No matching journal entries found.")

# --- Main CLI Loop ---

def main():
    while True:
        print("\n=== cineLog CLI ===")
        print("1. View all users")
        print("2. Add a user")
        print("3. Delete a user")
        print("4. Update a user")
        print("5. Exit")
        print("6. Add journal entry")
        print("7. View all journal entries")
        print("8. Search journal entries by title")
        print("9. Delete journal entry")

        choice = input("Select an option: ")

        if choice == "1":
            view_users()
        elif choice == "2":
            add_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            update_user()
        elif choice == "5":
            print("Goodbye!")
            break
        elif choice == "6":
            add_journal_entry()
        elif choice == "7":
            view_all_entries()
        elif choice == "8":
            search_entries()
        elif choice == "9":
            delete_entry()
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
