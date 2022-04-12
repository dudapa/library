from .config import consts
from .utils.postgres_handler import PostgresHandler


class LibrarySystem:
    def __init__(self, db_handler: PostgresHandler):
        self.db_handler=db_handler

    # Getting data
    def get_all_books(self):
        all_books = self.db_handler.get_all_data(consts.BOOKS_TABLE)
        return all_books
    
    def get_book_by_id(self, book_id):
        book = self.db_handler.get_selected_data(consts.BOOKS_TABLE, "book_id", book_id)
        return book

    def get_all_authors(self):
        all_authors = self.db_handler.get_all_data(consts.AUTHORS_TABLE)
        return all_authors
    
    def get_all_genres(self):
        all_genres = self.db_handler.get_all_data(consts.GENRES_TABLE)
        return all_genres

    def get_all_borrowers(self):
        all_borrowers = self.db_handler.get_all_data(consts.BORROWERS_TABLE)
        return all_borrowers

    def get_all_borrows(self):
        all_borrows = self.db_handler.get_all_data(consts.BORROWS_TABLE)
        return all_borrows

    def get_books_by_genre(self, genre_id):
        books = self.db_handler.join_tables([(consts.BOOKS_TABLE, "author_id", "genre_id"), (consts.AUTHORS_TABLE,  "author_id"), (consts.GENRES_TABLE, "genre_id")], (consts.GENRES_TABLE, "genre_id", str(genre_id)))
        return books

    def get_books_by_author(self, author_id):
        books = self.db_handler.join_tables([(consts.BOOKS_TABLE, "author_id", "genre_id"), (consts.AUTHORS_TABLE,  "author_id"), (consts.GENRES_TABLE, "genre_id")], (consts.AUTHORS_TABLE, "author_id", str(author_id)))
        return books
    
    def get_borrowed_books_by_borrower(self, borrower_id):
        books = self.db_handler.join_tables([(consts.BORROWS_TABLE, "borrower_id", "book_id"), (consts.BORROWERS_TABLE, "borrower_id"), (consts.BOOKS_TABLE, "book_id")], (consts.BORROWS_TABLE, "borrower_id", borrower_id))
        return books

    # Inserting data
    def insert_book(self, data_dict):
        self.db_handler.insert_data(consts.BOOKS_TABLE, data_dict)

    def insert_author(self, data_dict):
        return self.db_handler.insert_data(consts.AUTHORS_TABLE, data_dict)

    def insert_genre(self, data_dict):
        self.db_handler.insert_data(consts.GENRES_TABLE, data_dict)

    def insert_borrower(self, data_dict):
        self.db_handler.insert_data(consts.BORROWERS_TABLE, data_dict)

    # Transaction 
    def insert_borrow(self, borrower_id, book_id):
        self.db_handler.borrow_book(borrower_id, book_id)

    def return_book(self, book_id):
        self.db_handler.return_book(book_id)

    # Joining tables
    def join_tables(self, list_data):
        joined_tables = self.db_handler.join_tables(list_data)
        return joined_tables
