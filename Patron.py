from Person import Person
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
