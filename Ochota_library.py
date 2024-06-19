class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def __str__(self):
        return f"Name {self.name},id {self.id}"

class Patron(Person):
    def __init__(self, name, patron_id):
        super().__init__(name,patron_id)
        self.borrowed_books= []

    def borrow_book(self,book):
        if book.available:
            book.available=False
            self.borrowed_books.append(book)


    def return_book(self,book):
        if book.available :
            book.available=True
            self.borrowed_books.remove(book)


class Librarian(Person):
    def __init__(self, name, librarian_id):
        self.name= name
        self.librarian_id = librarian_id

    def add_book(self, library, book):
        library.add_books(book)
        print(f"{book.name} added by {self.name}")

    def remove_book(self, library, book):
        library.remove_book(book)
        print(f"{book.name} removed by {self.name}")

    def add_patron(self, library, patron):
        library.add_patron(patron)
        print(f"{patron.name} added as a patron by {self.name}")

    def remove_patron(self, library, patron):
        library.remove_patron(patron)
        print(f"{patron.name} removed as a patron by {self.name}")


class Book:
    def __init__(self,name,author,isbn,):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.available = True
        self.available= True

    def __str__(self):
        return f"Name:{self.name} author:{self.author} isbn:{self.isbn}"


class Library(Book):
    def __init__(self,name):
        self.name = name
        self.books= []
        self.patrons = []

    def add_books(self,book):
        self.books.append(book)

    def remove_books(self,book):
        if book in self.books:
            self.books.remove(book)

    def add_patron(self,patron):
        self.patrons.append(patron)

    def remove_patrons(self,patron):
        if patron in self.patrons:
            self.patrons.remove(patron)

    def list_books(self):
         for book in self.books:
             print(book)

    def list_patrons(self):
        for patron in self.patrons:
            print(patron)

print("welcome Warsaw library")
print("you can find every book in your mind in here")
library = Library("City Library")

book1 = Book("1984", "George Orwell", "9780451524935")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

patron1 = Patron("Alice", "P001")
patron2 = Patron("Bob", "P002")

librarian = Librarian("Emily", "L001")

librarian.add_book(library, book1)
librarian.add_book(library, book2)
librarian.add_patron(library, patron1)
librarian.add_patron(library, patron2)

patron1.borrow_book(book1)
patron2.borrow_book(book2)

library.list_books()
library.list_patrons()

patron1.return_book(book1)
patron2.return_book(book2)

library.list_books()
library.list_patrons()

print("")