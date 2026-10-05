class User:
    def __init__(self, name):
        self.name = name

    def borrow(self, book):
        print(self.name, "borrowed", book)


class Student(User):
    def borrow(self, book):
        print("Student", self.name, "borrowed", book, "for 7 days")


class Faculty(User):
    def borrow(self, book):
        print("Faculty", self.name, "borrowed", book, "for 30 days")


class Book:
    def __init__(self, title):
        self.title = title


book = Book("Artificial Intelligence")

users = [Student("Anu"), Faculty("Dr. Kumar")]

for user in users:
    user.borrow(book.title)