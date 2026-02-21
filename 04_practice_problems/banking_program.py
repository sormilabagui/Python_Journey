#python banking program

def show_balance(balance):
    print("----------------------")
    print(f"ur balance is ${balance:.2f}")
    print("----------------------")

def deposit():
    print("--------------------------------")
    amount = float(input("Enter an amount to deposit:"))
    print("--------------------------------")

    if amount < 0:
        print("-------------------------")
        print("That's not valid amount")
        print("-------------------------")
        return 0
    else:
        return amount


def withdraw(balance):
    print("--------------------------------")
    amount = float(input("enter amount to be withdraw:"))
    print("--------------------------------")
    if amount > balance:
        print("--------------------------------")
        print("insufficients funds")
        print("--------------------------------")
        return 0
    elif amount < 0:
        print("--------------------------------")
        print("amount must be greater then 0")
        print("--------------------------------")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("----------------")
        print("Banking program")
        print("----------------")
        print("1. SHow balance")
        print("2. Deposit")
        print("3. withdraw")
        print("4. Exit")
        print("----------------------")
        ch = input("Enter ur choice (1-4):")

        if ch == "1":
            show_balance(balance)
        elif ch == "2":
            balance += deposit()
        elif ch == "3":
            balance -= withdraw(balance)
        elif ch == "4":
            is_running = False
        else:
            print("--------------------------------")
            print("invalid option...")
            print("--------------------------------")

    print("----------------------")
    print("Thnaku have a nice day")
    print("----------------------")


if __name__ == "__main__":
    main()