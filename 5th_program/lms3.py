class Book:
    def __init__(self, title):
        self.title = title

    def access(self):
        print("Accessing:", self.title)


class PrintedBook(Book):
    def access(self):
        print("Issued printed book:", self.title)


class EBook(Book):
    def access(self):
        print("Downloading e-book:", self.title)


books = [
    PrintedBook("Marketing Management"),
    EBook("Digital Marketing")
]

for book in books:
    book.access()