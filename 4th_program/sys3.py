contacts = {}

name = input("Enter name: ")
phone = input("Enter phone: ")

contacts[name] = phone

delete = input("Enter name to delete: ")

if delete in contacts:
    del contacts[delete]
    print("Contact deleted")
else:
    print("Contact not found")

with open("contacts.txt", "w") as file:
    for n, p in contacts.items():
        file.write(n + " : " + p + "\n")