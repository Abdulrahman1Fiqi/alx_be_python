class Book:
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self.__is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self.__is_checked_out


class Library:
    def __init__(self):
        self.__books = []  # Private list to store Book instances

    def add_Book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)

    def check_out_Book(self, title):
        for book in self.__books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"The book '{title}' has been checked out.")
                    return
        print(f"The book '{title}' is not available for checkout.")

    def return_Book(self, title):
        for book in self.__books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"The book '{title}' has been returned.")
                    return
        print(f"The book '{title}' is not checked out.")

    def listavailablebooks(self):
        available_books = [book.title for book in self.__books if book.is_available()]
        if available_books:
            print("Available books:")
            for title in available_books:
                print(f"- {title}")
        else:
            print("No books are currently available.")