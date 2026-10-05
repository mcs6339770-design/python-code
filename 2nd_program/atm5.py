balance = 1000
pin = 1234

p = int(input("Enter PIN: "))

if p == pin:
    while True:
        print("\n1.Balance 2.Deposit 3.Withdraw 4.Exit")
        ch = int(input("Choice: "))

        if ch == 1:
            print("Balance:", balance)

        elif ch == 2:
            balance += int(input("Enter amount: "))

        elif ch == 3:
            amount = int(input("Enter amount: "))
            if amount <= balance:
                balance -= amount
            else:
                print("Insufficient balance")

        elif ch == 4:
            print("Thank you!")
            break

        else:
            print("Invalid choice")
else:
    print("Wrong PIN")