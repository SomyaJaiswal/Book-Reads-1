import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    books = csv.reader(f)
    db.execute("create table books (isbn varchar Primary Key,title Varchar ,author Varchar not null,year integer not null)")
    for isbn, title, author, year in books:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"Added book: {title} author: {author} year {year}")
    db.commit()

if __name__ == "__main__":
    main()