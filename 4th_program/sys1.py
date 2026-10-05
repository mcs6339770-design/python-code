contacts = {}

name = input("Enter name: ")
phone = input("Enter phone: ")

contacts[name] = phone

with open("contacts.txt", "w") as file:
    for name, phone in contacts.items():
        file.write(name + " : " + phone + "\n")

print("Contact saved successfully.")