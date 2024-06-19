from Person_Class import Person
from Person_Class import Patron
from Book_class import Book

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


print("welcome to the library")
print("you can find every book from your imagination")