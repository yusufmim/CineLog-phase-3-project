from tabulate import tabulate

def print_users(users):
    if not users:
        print("No users found.")
        return
    table = [(u.id, u.username) for u in users]
    print(tabulate(table, headers=["ID", "Username"], tablefmt="grid"))

def print_movie_nights(movie_nights):
    if not movie_nights:
        print("No movie nights found.")
        return
    table = [(mn.id, mn.date, mn.location) for mn in movie_nights]
    print(tabulate(table, headers=["ID", "Date", "Location"], tablefmt="grid"))

def print_movies(movies):
    if not movies:
        print("No movies found.")
        return
    table = [(m.id, m.title, m.genre or "-", m.rating or "-") for m in movies]
    print(tabulate(table, headers=["ID", "Title", "Genre", "Rating"], tablefmt="grid"))
