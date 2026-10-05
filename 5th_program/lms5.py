class LibraryItem:
    def __init__(self, name):
        self.name = name
        self.status = "Available"

    def issue(self):
        self.status = "Issued"
        print(self.name, "->", self.status)

    def return_item(self):
        self.status = "Available"
        print(self.name, "->", self.status)


class Book(LibraryItem):
    def issue(self):
        print("Book issue process")
        super().issue()


class Magazine(LibraryItem):
    def issue(self):
        print("Magazine issue process")
        super().issue()


items = [Book("Python"), Magazine("Business Today")]

for item in items:
    item.issue()

items[0].return_item()