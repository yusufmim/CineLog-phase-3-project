from datetime import datetime
from .database import get_session
from .crud import (
    create_user, get_all_users, get_user_by_username, delete_user,
    create_movie_night, get_movie_nights_by_user, delete_movie_night,
    create_movie, get_movies_by_movie_night, delete_movie
)
from .utils import print_users, print_movie_nights, print_movies

def main_menu():
    print("\n--- CineLog: Movie Night Organizer ---")
    print("1. Manage Users")
    print("2. Manage Movie Nights")
    print("3. Manage Movies")
    print("4. Exit")
    choice = input("Choose an option: ")
    return choice

def user_menu():
    print("\n--- User Management ---")
    print("1. Add User")
    print("2. List Users")
    print("3. Delete User")
    print("4. Back")
    choice = input("Choose an option: ")
    return choice

def movie_night_menu():
    print("\n--- Movie Night Management ---")
    print("1. Add Movie Night")
    print("2. List Movie Nights by User")
    print("3. Delete Movie Night")
    print("4. Back")
    choice = input("Choose an option: ")
    return choice

def movie_menu():
    print("\n--- Movie Management ---")
    print("1. Add Movie to Movie Night")
    print("2. List Movies by Movie Night")
    print("3. Delete Movie")
    print("4. Back")
    choice = input("Choose an option: ")
    return choice

def cli():
    db = get_session()
    while True:
        choice = main_menu()
        if choice == "1":
            while True:
                c = user_menu()
                if c == "1":
                    username = input("Enter new username: ").strip()
                    if username:
                        if get_user_by_username(db, username):
                            print("Username already exists.")
                        else:
                            user = create_user(db, username)
                            print(f"User '{user.username}' added with ID {user.id}.")
                    else:
                        print("Username cannot be empty.")
                elif c == "2":
                    users = get_all_users(db)
                    print_users(users)
                elif c == "3":
                    uid = input("Enter User ID to delete: ").strip()
                    if uid.isdigit():
                        if delete_user(db, int(uid)):
                            print("User deleted.")
                        else:
                            print("User not found.")
                    else:
                        print("Invalid ID.")
                elif c == "4":
                    break
                else:
                    print("Invalid option.")

        elif choice == "2":
            while True:
                c = movie_night_menu()
                if c == "1":
                    uid = input("Enter User ID to associate movie night with: ").strip()
                    if not uid.isdigit():
                        print("Invalid User ID.")
                        continue
                    from datetime import datetime
                    date_str = input("Enter date of movie night (YYYY-MM-DD): ").strip()
                    try:
                        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format.")
                        continue
                    location = input("Enter location of movie night: ").strip()
                    if location == "":
                        print("Location cannot be empty.")
                        continue
                    mn = create_movie_night(db, int(uid), date_obj, location)
                    print(f"Movie Night added with ID {mn.id}.")
                elif c == "2":
                    uid = input("Enter User ID to list movie nights: ").strip()
                    if uid.isdigit():
                        mns = get_movie_nights_by_user(db, int(uid))
                        print_movie_nights(mns)
                    else:
                        print("Invalid ID.")
                elif c == "3":
                    mnid = input("Enter Movie Night ID to delete: ").strip()
                    if mnid.isdigit():
                        if delete_movie_night(db, int(mnid)):
                            print("Movie Night deleted.")
                        else:
                            print("Movie Night not found.")
                    else:
                        print("Invalid ID.")
                elif c == "4":
                    break
                else:
                    print("Invalid option.")

        elif choice == "3":
            while True:
                c = movie_menu()
                if c == "1":
                    mnid = input("Enter Movie Night ID to add movie to: ").strip()
                    if not mnid.isdigit():
                        print("Invalid Movie Night ID.")
                        continue
                    title = input("Enter movie title: ").strip()
                    genre = input("Enter genre (optional): ").strip()
                    rating_str = input("Enter rating (1-10, optional): ").strip()
                    rating = None
                    if rating_str.isdigit():
                        r = int(rating_str)
                        if 1 <= r <= 10:
                            rating = r
                        else:
                            print("Rating must be between 1 and 10.")
                            continue
                    movie = create_movie(db, int(mnid), title, genre or None, rating)
                    print(f"Movie '{movie.title}' added with ID {movie.id}.")
                elif c == "2":
                    mnid = input("Enter Movie Night ID to list movies: ").strip()
                    if mnid.isdigit():
                        movies = get_movies_by_movie_night(db, int(mnid))
                        print_movies(movies)
                    else:
                        print("Invalid ID.")
                elif c == "3":
                    mid = input("Enter Movie ID to delete: ").strip()
                    if mid.isdigit():
                        if delete_movie(db, int(mid)):
                            print("Movie deleted.")
                        else:
                            print("Movie not found.")
                    else:
                        print("Invalid ID.")
                elif c == "4":
                    break
                else:
                    print("Invalid option.")
        elif choice == "4":
            print("Exiting... Goodbye!")
            db.close()
            break
        else:
            print("Invalid option.")
