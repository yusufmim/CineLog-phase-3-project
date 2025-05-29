from cinelog import cli
from cinelog.database import engine, Base

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

def main():
    create_db_and_tables()
    cli.cli()

if __name__ == "__main__":
    main()
