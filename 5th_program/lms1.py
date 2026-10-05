class User:
    def __init__(self, name):
        self.name = name

    def limit(self):
        return 2


class Student(User):
    def limit(self):
        return 3


class Teacher(User):
    def limit(self):
        return 5


class Book:
    def __init__(self, title):
        self.title = title
        self.issued = False

    def issue(self, user):
        if not self.issued:
            self.issued = True
            print(user.name, "issued", self.title)
        else:
            print("Book already issued")

    def return_book(self):
        self.issued = False
        print(self.title, "returned")


s = Student("Arun")
t = Teacher("Meena")
b = Book("Python Programming")

b.issue(s)
b.return_book()
b.issue(t)