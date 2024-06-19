from Person_Class import Person
from Person_Class import Patron
from Book_class import Book




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
