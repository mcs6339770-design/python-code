balance = 1000

while True:
    print("\n1. Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance =", balance)
    elif choice == 2:
        amount = int(input("Enter deposit: "))
        balance += amount
        print("Deposited successfully")
    elif choice == 3:
        amount = int(input("Enter withdrawal: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice")