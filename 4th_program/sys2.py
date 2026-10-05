contacts = {}

name = input("Enter name: ")
phone = input("Enter phone: ")

contacts[name] = phone

search = input("Search name: ")

if search in contacts:
    print("Phone:", contacts[search])
else:
    print("Contact not found")

with open("contacts.txt", "w") as file:
    for n, p in contacts.items():
        file.write(n + "," + p + "\n")