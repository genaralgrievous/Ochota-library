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