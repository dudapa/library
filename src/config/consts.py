import os


# Table constants 
BORROWERS_TABLE=os.getenv("BORROWERS_TABLE", "borrowers")
AUTHORS_TABLE=os.getenv("AUTHORS_TABLE", "authors")
GENRES_TABLE=os.getenv("GENRES_TABLE", "genres")
BOOKS_TABLE=os.getenv("BOOKS_TABLE", "books")
BORROWS_TABLE=os.getenv("BORROWS_TABLE", "borrows")

# Database constants 
POSTGRES_HOST=os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_DATABASE=os.getenv("POSTGRES_DATABASE", "postgres")
POSTGRES_USER=os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD", "postgres")
