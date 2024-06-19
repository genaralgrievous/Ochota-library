class Librarian(person):
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