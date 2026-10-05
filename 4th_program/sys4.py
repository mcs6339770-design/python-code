contacts = []

name = input("Enter name: ")
phone = input("Enter phone: ")

contact = [name, phone]
contacts.append(contact)

print("Contact added.")

for contact in contacts:
    print("Name:", contact[0])
    print("Phone:", contact[1])

with open("contacts.txt", "w") as file:
    for contact in contacts:
        file.write(contact[0] + " " + contact[1] + "\n")