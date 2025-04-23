class Book:
#Create the Book Class: Create the __init__(self, title, author) method Set .title and .author to the values of the parameters.
    def __init__(self, title, author):
        self.title = title
        self.author = author

#Create the library class 
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_books(self, search_string):
        found_books = []
        for book in self.books:
            if search_string.lower() in book.title.lower() or search_string.lower() in book.author.lower():
                found_books.append(book)
        return found_books
