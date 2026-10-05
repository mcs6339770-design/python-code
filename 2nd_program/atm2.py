balance = 1000

def atm():
    global balance

    while True:
        print("\n1.Balance  2.Deposit  3.Withdraw  4.Exit")
        ch = int(input("Choice: "))

        if ch == 1:
            print("Balance:", balance)
        elif ch == 2:
            balance += int(input("Deposit: "))
        elif ch == 3:
            money = int(input("Withdraw: "))
            if money <= balance:
                balance -= money
            else:
                print("Insufficient balance")
        elif ch == 4:
            break
        else:
            print("Invalid choice")

atm()