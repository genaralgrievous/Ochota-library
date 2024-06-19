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


