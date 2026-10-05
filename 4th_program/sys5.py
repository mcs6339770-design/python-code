contacts = {}

while True:
    print("\n1. Add")
    print("2. Search")
    print("3. Delete")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == "2":
        name = input("Enter name: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":
        with open("contacts.txt", "w") as file:
            for name, phone in contacts.items():
                file.write(name + " : " + phone + "\n")

        print("Contacts saved.")
        break

    else:
        print("Invalid choice.")