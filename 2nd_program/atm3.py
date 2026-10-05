balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            print("Balance:", balance)

        case 2:
            balance += int(input("Enter amount: "))
            print("Deposit successful")

        case 3:
            amount = int(input("Enter amount: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")

        case 4:
            print("Thank you!")
            break

        case _:
            print("Invalid choice")