class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def __str__(self):
        return f'{self.author}, {self.title}'

    def __eq__(self, other):
        return self.author == other.author and self.title == other.title


class Bookcase:

    def __init__(self):
        self.books = []

    def __iter__(self):
        yield from self.books

    def add_book(self, book):
        self.books.append(book)

book1  = Book("titulo1", 'auto1')

bookcase = Bookcase()
bookcase.add_book(book1)

for book in bookcase:
    print(book)
