from LIbrarian_class import Librarian
from Book_class import Book
from Person_Class import Person
from Person_Class import Patron
from Library_class import Library

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