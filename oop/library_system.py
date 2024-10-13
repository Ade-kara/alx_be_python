class Book:
    def __init__(self, title, author):
        """Initialize the Book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of the Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize the EBook attributes, including those from Book."""
        super().__init__(title, author)
        self.file_size = file_size  # Size in KB

    def __str__(self):
        """String representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize the PrintBook attributes, including those from Book."""
        super().__init__(title, author)
        self.page_count = page_count  # Number of pages

    def __str__(self):
        """String representation of the PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)


# The library_system.py file contains class definitions for Book, EBook, PrintBook, and Library.