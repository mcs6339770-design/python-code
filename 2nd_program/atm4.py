b = 1000

while True:
    c = input("\nB-Balance D-Deposit W-Withdraw E-Exit: ").upper()

    if c == "B":
        print("Balance:", b)

    elif c == "D":
        b += int(input("Amount: "))

    elif c == "W":
        x = int(input("Amount: "))
        if x <= b:
            b -= x
        else:
            print("Insufficient balance")

    elif c == "E":
        print("Thank you")
        break

    else:
        print("Wrong choice")