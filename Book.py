from Person_Class import Patron

class Book:
    def __init__(self,name,author,isbn,):
        self.title = name
        self.author = author
        self.isbn = isbn
        self.available = True
        self.available= True

    def __str__(self):
        return f"Name:{self.name} author:{self.author} isbn:{self.isbn}"


class Library:
    def __init__(self,name):
        self.name = name
        books = ["karamazov brothers","peter pan","harry potter"]
        patrons = []

    def add_books(self,book):
        self.books.append(book)

    def remove_books(self,book):
        if book in self.books:
            self.books.remove(book)

    def add_patrons(self):
        self.patrons.append(Patron)

    def remove_patrons(self):
        if Patron in self.patrons:
            self.patrons.remove(Patron)

    def list_books(self):
         for book in self.books:
             print(book)

    def list_patrons(self):
        for patron in self.patrons:
            print(patron)
