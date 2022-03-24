INSERT INTO genres ("name")
VALUES ('Art, Architecture & Photography');
INSERT INTO genres ("name")
VALUES ('Biography');
INSERT INTO genres ("name")
VALUES ('Business');
INSERT INTO genres ("name")
VALUES ('Fiction');
INSERT INTO genres ("name")
VALUES ('History');
INSERT INTO genres ("name")
VALUES ('Romance');
INSERT INTO genres ("name")
VALUES ('Mystery & Crime');
INSERT INTO genres ("name")
VALUES ('Sports');

INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Andy', 'Warhol', '1928-02-02', 'US');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Vincent', 'van Gogh', '1853-03-30', 'NL');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Jimmy', 'Chin', '1968-10-03', 'US');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Kassia', 'St. Clair', '1980-01-15', 'US');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Alex', 'Kershaw', '1925-06-22', 'US');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Alex', 'Kershaw', '1925-06-22', 'US');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Kate', 'Moore', '1944-01-24', 'UK');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Tara', 'Westover', '1985-07-11', 'CND');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Peter', 'Regan', '1966-12-05', 'US');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Juld', 'Kahn', '1986-12-05', 'US');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Robert T.', 'Kiyosaki', '1956-10-22', 'JPN');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Nita', 'Prose', '1980-08-22', 'DE');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Sara', 'Bleedel', '1970-06-16', 'DE');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Jack', 'Stone', '1990-07-03', 'US');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Katrine', 'Engberg', '1970-10-03', 'DE');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Jennifer', 'Armentrout', '1977-11-23', 'US');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('James', 'Patron', '1922-11-13', 'US');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Serhii', 'Plokhy', '1975-05-11', 'UK');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Elena', 'Armas', '1985-05-06', 'AUS');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Ali', 'Armas', '1990-02-26', 'CDN');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Lisa', 'Barr', '1984-12-26', 'USA');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Alaina', 'Urquhart', '1975-09-11', 'UK');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Paul', 'McCartney', '1982-07-25', 'USA');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Jack', 'Tudor', '1942-07-05', 'USA');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Stephen', 'Chbosky', '19478-08-05', 'AUS');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Christopfer', 'Clarey', '1985-01-25', 'UK');
INSERT INTO authors ("name", surname, birthdate, nationality)
VALUES ('Jocko', 'Willink', '1971-09-21', 'US');

INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Andy Warhol Diaries', 255, 1, 1, 5);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Twelve Van Gogh Bookmarks', 400, 2, 1, 2);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('There and Back: Photographs from the Edge', 185, 3, 1, 3);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Secret Lives of Color', 300, 4, 1, 6);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Devil in the White City', 270, 4, 1, 10);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Against All Odds', 321, 5, 2, 3);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Woman They Could Not Silence', 233, 6, 2, 12);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Educated: A Memoir', 283, 7, 2, 3);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Boys', 299, 8, 2, 1);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Value Investing', 456, 9, 3, 2);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Rich Dad Poor Dad', 230, 10, 3, 15);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Maid', 300, 11, 4, 10);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Nature', 350, 11, 4, 8);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('A Harmless Lie', 354, 12, 4, 3);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Boy On The Moon', 116, 13, 4, 4);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The War of Two Queens', 350, 14, 5, 6);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Harbour', 554, 14, 5, 1);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('1941', 350, 15, 5, 6);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Franklin Winstone', 554, 16, 5, 5);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Gates of Europe', 650, 18, 5, 6);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Spanish Love Deception', 452, 19, 6, 20);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Love on The Moon', 520, 19, 6, 14);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Love Hypothesis', 351, 20, 6, 8);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Old Love', 251, 20, 6, 3);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Woman on Fire', 259, 21, 6, 4);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Man in The Forest', 262, 21, 6, 4);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Butcher and the Wren', 399, 22, 7, 6);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Lock Every Door', 560, 22, 7, 5);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Hollow Places', 532, 22, 7, 5);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Lyrics', 529, 23, 7, 4);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Silence in Fog', 429, 23, 7, 2);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Last Twilight ', 559, 23, 7, 4);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Burning Girls', 219, 24, 7, 4);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Imaginary Friend', 369, 25, 7, 7);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('The Master', 180, 26, 8, 2);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Real Madrid', 120, 26, 8, 3);
INSERT INTO books ("name", page_count, author_id, genre_id, book_count)
VALUES ('Breathe', 260, 27, 8, 4);
