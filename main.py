from src.library_system import LibrarySystem
from src.utils.postgres_handler import PostgresHandler
from src.config import consts


pg_handler = PostgresHandler(
    host=consts.POSTGRES_HOST,
    database=consts.POSTGRES_DATABASE,
    user=consts.POSTGRES_USER,
    password=consts.POSTGRES_PASSWORD
)

library_system = LibrarySystem(pg_handler)
 
def print_menu():
    print("\n***************************************")
    print("WELCOME TO THE LIBRARY")
    print("Select option from menu:")
    print("\t[0] borrow a book")
    print("\t[1] create a new borrower")
    print("\t[2] create a new book")
    print("\t[3] return a book")
    print("\t[4] show books")
    print("\t[5] show all borrowers")
    print("\t[6] terminate Library System")
    print()

def print_book_list(books):
    for id, book in enumerate(books):
        print(f"\tbook id: {id}")
        print(f"\tname: {book['book_name']}")
        print(f"\tpage count: {book['page_count']} str.")
        print(f"\tbook count: {book['book_count']}")
        print(f"\tauthor name: {book['author_name']} {book['author_surname']}")
        print(f"\tgenre: {book['genre_name']}")
        print()
    
def print_borrowed_book_list(books):
    print("------------------------------------------------------")
    print(f"{books[0]['firstname']} {books[0]['surname']}:")
    for id, book in enumerate(books):
        print(f"id: {id}\tname: {book['book_name']} {book['book_id']}")
    print("------------------------------------------------------")

def print_genre_list(genres):
    for id, genre in enumerate(genres):
        print(f"\tgenre id: {id}")
        print(f"\tgenre: {genre['genre_name']}")
        print()

def print_author_list(authors):
    for id, author in enumerate(authors):
        print(f"\tauthor id: {id}")
        print(f"\tname: {author['author_name']} {author['author_surname']}")
        print(f"\tbirthdate: {author['birthdate']}")
        print(f"\tnationality: {author['nationality']}")
        print()

def print_borrower_list(borrowers):
    for id, borrower in enumerate(borrowers):
        print(f"\tborrower id: {id}")
        print(f"\tname: {borrower['firstname']}")
        print(f"\tsurname: {borrower['surname']}")
        print(f"\tbirthdate: {borrower['birthdate']}")
        print(f"\tgender: {borrower['gender']}")
        print()

def print_author_list(authors):
    for id, author in enumerate(authors):
        print(f"\tauthor id: {id}")
        print(f"\tname: {author['author_name']}")
        print(f"\tsurname: {author['author_surname']}")
        print(f"\tbirthdate: {author['birthdate']}")
        print(f"\tnationality: {author['nationality']}")
        print()

def show_all_books(library_system: LibrarySystem, select_book=True):
    all_books = library_system.join_tables([("books", "author_id", "genre_id"), ("authors", "author_id"), ("genres", "genre_id")])

    print_book_list(all_books)
    if select_book:
        while True:
            try:
                book_id = int(input("Select book by its id that you want to borrow: "))
                if book_id < 0 or book_id >= len(all_books):
                    raise Exception(f"book id: {book_id} does not exist!")
            except Exception as e:
                print(e)
                print("Error during selection book id. Please repeat your choice.")
                continue
            break
        
        return all_books[book_id]["book_id"], all_books[book_id]["book_count"]

def show_books_by_genre(library_system: LibrarySystem, select_book=True):
    all_genres = library_system.get_all_genres()
    print_genre_list(all_genres)
    while True:
        try:    
            selected_genre = int(input("Select a genre by id: "))
            if selected_genre < 0 or selected_genre >= len(all_genres):
                raise Exception(f"genre id: {selected_genre} does not exist!") 
        except Exception as e:
            print(e)
            print("Error during selection genre. Please repeat your choice.")
            continue
        break
    books_by_genre = library_system.get_books_by_genre(selected_genre + 1)
    print_book_list(books_by_genre)
    if select_book:
        while True:
            try:
                book_id = int(input("Select book by its id that you want to borrow: "))
                if book_id < 0 or book_id >= len(books_by_genre):
                    raise Exception(f"book id: {book_id} does not exist!")
            except Exception as e:
                print(e)
                print("Error during selection book id. Please repeat your choice.")
                continue
            break
        return books_by_genre[book_id]["book_id"], books_by_genre[book_id]["book_count"]

def show_books_by_author(library_system: LibrarySystem, select_book=True):
    all_authors = library_system.get_all_authors()
    print_author_list(all_authors)
    while True:
        try:
            selected_author = int(input("Select an author by id: "))
            if selected_author < 0 or selected_author >= len(all_authors):
                raise Exception(f"author id: {selected_author} does not exist!")
        except Exception as e:
            print(e)
            print("Error during selection author. Please repeat your choice.")
            continue
        break

    books_by_author = library_system.get_books_by_author(selected_author + 1)
    print_book_list(books_by_author)

    if select_book:
        while True:
            try:
                book_id = int(input("Select book by its id that you want to borrow: "))
                if book_id < 0 or book_id >= len(books_by_author):
                    raise Exception(f"book id: {book_id} does not exist!")
            except Exception as e:
                print(e)
                print("Error during selection book id. Please repeat your choice.")
                continue
            break
        return books_by_author[book_id]["book_id"], books_by_author[book_id]["book_count"]

def create_borrower(library_system: LibrarySystem):
    while True:
        try:
            firstname = input("Enter borrower name: "),
            surname = input("Enter borrower surname: "),
            birthdate = input("Enter borrower birthdate (yyyy-mm-dd): ")
            gender = input("Enter borrower gender (f/m): ")
            if not firstname or not surname or not birthdate or not gender:
                raise Exception("You did not fill up parameters about a new borrower.")
        except Exception as e:
            print(e)
            print("Error during borrower insertion.")
            print("Please, reenter information about a new borrower.")
            continue
        break
    borrower_dict = {
        "firstname": firstname,
        "surname": surname,
        "birthdate": birthdate,
        "gender": gender
    }
    library_system.insert_borrower(borrower_dict)

def show_all_borrowers(library_system: LibrarySystem, select_borrower=False):
    all_borrowers = library_system.get_all_borrowers()
    print_borrower_list(all_borrowers)
    if select_borrower:
        while True:
            try:
                borrower_id = int(input(f"Select borrower by its id: "))
                if borrower_id < 0 or  borrower_id >= len(all_borrowers):
                    raise Exception(f"borrower id: {borrower_id} does not exist!")
            except Exception as e:
                print(e)
                print("Error during selection borrower id. Please repeat your choice.")
                continue
            break
        return all_borrowers[borrower_id]["borrower_id"]

def create_author(library_system: LibrarySystem):
    while True:
        try:
            author_name = input("Enter author name: ")
            author_surname = input("Eneter author surname: ")
            birthdate = input("Enter author birthdate (yyyy-mm-dd): ")
            nationality = input("Enter author nationality (eg. US, DE, CZ): ")
            if not author_name or not author_surname or not birthdate or not nationality:
                raise Exception("You did not fill up parameters about a new author.")
        except Exception as e:
            print(e)
            print("Error during author insertion.")
            print("Please, reenter information about a new author.")
            continue
        break

    author_dict = {
        "author_name": author_name,
        "author_surname": author_surname,
        "birthdate": birthdate,
        "nationality": nationality
    }

    new_borrower = library_system.insert_author(author_dict)
    return new_borrower["author_id"]

def show_all_authors(library_system: LibrarySystem, select_author=False):
    all_authors = library_system.get_all_authors()
    print_author_list(all_authors)
    if select_author:
        while True:
            try: 
                author_id = int(input(f"Select author by its id: "))
                if author_id < 0 or author_id >= len(all_authors):
                    raise Exception(f"author id: {author_id} does not exist!")
            except Exception as e:
                print(e)
                print("Error during selection author id. Please repeat your choice.")
                continue
            break
        return all_authors[author_id]["author_id"]
    
def show_books(library_system: LibrarySystem):
    print("\t[0] show all books")
    print("\t[1] show books by genre")
    print("\t[2] show books by author")
    while True:
        try:
            user_chiose = int(input("Select an option above: "))
            if user_chiose < 0 or user_chiose > 2:
                raise Exception("This option does not exit!")
            break
        except Exception as e:
            print(e)
            print("Please repeat your choice")
            continue
    if user_chiose == 0:
        show_all_books(library_system, select_book=False)
    if user_chiose == 1:
        show_books_by_genre(library_system, select_book=False)
    if user_chiose == 2:
        show_books_by_author(library_system, select_book=False)
    return None

def borrow_book(library_system: LibrarySystem):
    print("\t[0] show all books")
    print("\t[1] show books by genre")
    print("\t[2] show books by author")
    while True:
        try:
            user_chiose = int(input("Select an option above: "))
            if user_chiose < 0 or user_chiose > 2:
                raise Exception("This option does not exit!")
            break
        except Exception as e:
            print(e)
            print("Please repeat your choice")
            continue
    if user_chiose == 0:
        book_id, book_count = show_all_books(library_system)
        if int(book_count) == 0:
            print("-------------------------------------------------------------------------")
            print("This book is not in stock at the moment. You have to await for this book.")
            print("-------------------------------------------------------------------------")
            return None
    if user_chiose == 1:
        book_id, book_count = show_books_by_genre(library_system)
        if int(book_count) == 0:
            print("-------------------------------------------------------------------------")
            print("This book is not in stock at the moment. You have to await for this book.")
            print("-------------------------------------------------------------------------")
            return None
    if user_chiose == 2:
        book_id, book_count = show_books_by_author(library_system)
        if int(book_count) == 0:
            print("-------------------------------------------------------------------------")
            print("This book is not in stock at the moment. You have to await for this book.")
            print("-------------------------------------------------------------------------")
            return None

    borrower_id = show_all_borrowers(library_system, select_borrower=True)
    library_system.insert_borrow(borrower_id, book_id)
    return True

def return_book(library_system: LibrarySystem):
    print("Return a book as a borrower:\n")
    borrower_id = show_all_borrowers(library_system, select_borrower=True)
    borrowed_books = library_system.get_borrowed_books_by_borrower(borrower_id)
    not_return_books = [book for book in borrowed_books if not book["return_date"]]

    if len(not_return_books) == 0:
        print("--------------------------------------------")
        print("Selected borrower does not have any borrows.")
        print("--------------------------------------------")
        return None

    print_borrowed_book_list(not_return_books)
    while True:
        try:
            user_choice = int(input("Select book by its id: "))
            if user_choice < 0 or user_choice >= len(not_return_books):
                raise Exception(f"book id: {user_choice} does not exist!")
        except Exception as e:
            print(e)
            print("Error during selection book id. Please repeat your choice.")
            continue
        break
    book_id = not_return_books[user_choice]["book_id"]
    library_system.return_book(book_id)
    return True

def create_new_book(library_system: LibrarySystem):
    all_genres = library_system.get_all_genres()
    print_genre_list(all_genres)
    while True:
        try:
            user_choice = int(input("What a genre is a new book (select genre id): "))
            if user_choice < 0 or user_choice >= len(all_genres):
                raise Exception(f"genre id: {user_choice} does not exist!")
            genre_id = all_genres[user_choice]["genre_id"]
            print(f"id: {genre_id}")
        except Exception as e:
            print(e)
            print("Error during selection genre id. Please repeat your choice.")
            continue
        break
    
    print("\n[0] Create a new autor.")
    print("[1] Select an author from database.")
    
    while True:
        try:
            user_choice2 = int(input("Select one option above: "))
            if user_choice2 < 0 or user_choice2 > 1:
                raise Exception("Your option does not exist!")
        except Exception as e:
            print(e)
            print("Try to enter your choice again: ")
            continue
        break
    
    if user_choice2 == 0:
        author_id = create_author(library_system)
    if user_choice2 == 1:
        author_id = show_all_authors(library_system, select_author=True)

    while True:
        try:
            book_name = input("Enter book name: ")
            page_count = input("Enter number of pages: ")
            book_count = input("Enter number of books in the library stock: ")
            if not book_name or not page_count or not book_count:
                raise Exception("You did not fill up parameters about a new book.")
        except Exception as e:
            print(e)
            print("Error during book insertion. Please reenter data.")
            continue
        break
    book_dict = {
        "book_name": book_name,
        "page_count": page_count,
        "author_id": author_id,
        "genre_id": genre_id,
        "book_count": book_count
    }

    library_system.insert_book(book_dict)
    return True


if __name__ == "__main__":
    while True:
        while True:
            try:
                print_menu()
                user_choice = int(input("Select one option from menu: "))
                if user_choice < 0 or user_choice > 6:
                    raise Exception("This option does not exit!")
                break
            except Exception as e:
                print(e)
                print("Please repeat your choice")

        if user_choice == 0:
            borrow_book(library_system)
        if user_choice == 1:
            create_borrower(library_system)
        if user_choice == 2:
            create_new_book(library_system)
        if user_choice == 3:
            return_book(library_system)
        if user_choice == 4:
            show_books(library_system)
        if user_choice == 5:
            show_all_borrowers(library_system)
        if user_choice == 6:
            print("Goodbye my friend!!!")
            break
        