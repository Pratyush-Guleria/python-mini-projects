def show_menu():
    print("\n--- MENU ---")
    print("1. Cash Deposit")
    print("2. Cash Withdraw")
    print("3. Exit")

def deposit(balance, name):
    print(f"\nHey {name}, your current balance is: ${balance}")
    amount = float(input("Enter amount to deposit: $"))
    balance += amount
    print("✔ Deposit successful!")
    print(f"Updated Balance: ${balance}")
    return balance


def withdraw(balance, name):
    print(f"\nYour current balance is: ${balance}")
    amount = float(input("Enter amount to withdraw: $"))

    if amount > balance:
        print("⚠ Insufficient balance!")
        return balance

    balance -= amount
    print(f"✔ Withdrawal of ${amount} completed!")
    print(f"Updated Balance: ${balance}")
    return balance


print("Welcome to our Mini Bank")
name = input("Enter your name: ")
balance = float(input("Enter your initial balance: $"))

while True:
    show_menu()
    option = input("Choose an option: ")

    if option == "1":
        balance = deposit(balance, name)

    elif option == "2":
        balance = withdraw(balance, name)

    elif option == "3":
        confirm = input(f"Hey {name}, do you really want to exit? (Y/N): ")
        if confirm.upper() == "Y":
            print("Thank you for coming 😊")
            break
        else:
            continue
    else:
        print("Invalid option. Please choose again.")