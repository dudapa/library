import psycopg2
from psycopg2 import sql
import sys
sys.path.insert(0, 'C:\\Users\\duzda\\Desktop\\library\\src\\config')
import consts


if __name__ == "__main__":
    print("-----TABLES WILL BE CREATED-----")
    conn=psycopg2.connect(
        host=consts.POSTGRES_HOST,
        database=consts.POSTGRES_DATABASE,
        user=consts.POSTGRES_USER,
        password=consts.POSTGRES_PASSWORD
    )
    print("-----CONNECTED TO DATABASE-----")

    with conn, conn.cursor() as cursor:
        create_borrowers_table_query=sql.SQL(
            """
            DROP TABLE IF EXISTS borrowers CASCADE;

            CREATE TABLE borrowers (
                borrower_id serial PRIMARY KEY,
                name VARCHAR(128) NOT NULL,
                surname VARCHAR(128) NOT NULL,
                birtdate DATE NOT NULL,
                gender VARCHAR(16) NOT NULL
            );
            """
        )
        print(create_borrowers_table_query.as_string(cursor))
        cursor.execute(create_borrowers_table_query)
        
        create_authors_table_query=sql.SQL(
            """
            DROP TABLE IF EXISTS authors CASCADE;

            CREATE TABLE authors (
                author_id serial PRIMARY KEY,
                name VARCHAR(128) NOT NULL,
                surname VARCHAR(128) NOT NULL,
                birthdate DATE NOT NULL,
                nationality VARCHAR(128) NOT NULL
            );
            """
        )
        print(create_authors_table_query.as_string(cursor))
        cursor.execute(create_authors_table_query)

        create_genres_table_query=sql.SQL(
            """
            DROP TABLE IF EXISTS genres CASCADE;

            CREATE TABLE genres (
                genre_id serial PRIMARY KEY,
                name VARCHAR(128) NOT NULL
            );
            """
        )
        print(create_genres_table_query.as_string(cursor))
        cursor.execute(create_genres_table_query)

        create_books_table_query=sql.SQL(
            """
            DROP TABLE IF EXISTS books CASCADE;

            CREATE TABLE books (
                book_id serial PRIMARY KEY,
                name VARCHAR(128) NOT NULL,
                page_count INT NOT NULL,
                author_id INT NOT NULL,
                genre_id INT NOT NULL,
                book_count INT NOT NULL,
                CONSTRAINT fk_author FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE ON UPDATE NO ACTION,
                CONSTRAINT fk_genre FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE ON UPDATE NO ACTION
            );
            """
        )
        print(create_books_table_query.as_string(cursor))
        cursor.execute(create_books_table_query)

        create_borrows_table_query=sql.SQL(
            """
            DROP TABLE IF EXISTS borrows CASCADE;

            CREATE TABLE borrows (
                borrow_id serial PRIMARY KEY,
                borrower_id INT NOT NULL,
                book_id INT NOT NULL,
                borrow_date DATE NOT NULL,
                return_date DATE,
                CONSTRAINT fk_borrower FOREIGN KEY (borrower_id) REFERENCES borrowers(borrower_id) ON DELETE CASCADE ON UPDATE NO ACTION,
                CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE ON UPDATE NO ACTION
            );
            """
        )
        print(create_borrows_table_query.as_string(cursor))
        cursor.execute(create_borrows_table_query)
    
    conn.close()
    print("-----TABLES WAS CREATED-----")
