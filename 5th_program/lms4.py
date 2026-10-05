class User:
    def __init__(self, name):
        self.name = name

    def borrow_limit(self):
        return 0


class Student(User):
    def borrow_limit(self):
        return 2


class Researcher(User):
    def borrow_limit(self):
        return 5


class Librarian(User):
    def borrow_limit(self):
        return 10


class Library:
    def issue(self, user, book):
        print(user.name, "can borrow", user.borrow_limit(), "books")
        print("Issued:", book)


library = Library()

users = [
    Student("Ravi"),
    Researcher("Priya"),
    Librarian("Karthik")
]

for u in users:
    library.issue(u, "Python Programming")