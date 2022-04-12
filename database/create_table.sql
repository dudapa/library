DROP TABLE IF EXISTS borrowers CASCADE;

CREATE TABLE borrowers (
	borrower_id serial PRIMARY KEY,
	firstname VARCHAR(128) NOT NULL,
	surname VARCHAR(128) NOT NULL,
	birthdate DATE NOT NULL,
	gender VARCHAR(16) NOT NULL
);


DROP TABLE IF EXISTS authors CASCADE;

CREATE TABLE authors (
	author_id serial PRIMARY KEY,
	author_name VARCHAR(128) NOT NULL,
	author_surname VARCHAR(128) NOT NULL,
	birthdate DATE NOT NULL,
	nationality VARCHAR(128) NOT NULL
);


DROP TABLE IF EXISTS genres CASCADE;

CREATE TABLE genres (
	genre_id serial PRIMARY KEY,
	genre_name VARCHAR(128) NOT NULL
);


DROP TABLE IF EXISTS books CASCADE;

CREATE TABLE books (
	book_id serial PRIMARY KEY,
	book_name VARCHAR(128) NOT NULL,
	page_count INT NOT NULL,
	author_id INT NOT NULL,
	genre_id INT NOT NULL,
	book_count INT NOT NULL,
	CONSTRAINT fk_author FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE ON UPDATE NO ACTION,
	CONSTRAINT fk_genre FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE ON UPDATE NO ACTION
);


DROP TABLE IF EXISTS borrows CASCADE;

CREATE TABLE borrows (
	borrower_id INT NOT NULL,
	book_id INT NOT NULL,
	borrow_date DATE DEFAULT CURRENT_DATE,
	return_date DATE,
	CONSTRAINT pk_borrower_book PRIMARY KEY (borrower_id, book_id),
	CONSTRAINT fk_borrower FOREIGN KEY (borrower_id) REFERENCES borrowers(borrower_id) ON DELETE CASCADE ON UPDATE NO ACTION,
	CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE ON UPDATE NO ACTION
);
