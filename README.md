# cineLog

**cineLog** is a command-line application for managing a movie review database. Built using Python, SQLAlchemy, and Alembic, it allows users to add, browse, and review movies, all from a simple terminal interface.

---

##  Features

-  **Movie Management**: Add new movies with title, genre, and release year.
-  **User Accounts**: Create and list users.
-  **Reviews**: Users can submit reviews for movies with ratings and comments.
-  **Data Persistence**: All data is stored in an SQLite database using SQLAlchemy ORM.
-  **Database Migrations**: Managed with Alembic for smooth schema evolution.
-  **Dependency Management**: Uses Pipenv for virtual environments and package control.

---

## Technologies Used

- **Python 3**
- **SQLAlchemy** – ORM for database interactions
- **Alembic** – For schema migrations
- **Tabulate** – To display output in tables
- **Pipenv** – For managing dependencies and virtual environment
- **SQLite** – Lightweight database

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yusufmim/cineLog.git
cd cineLog
