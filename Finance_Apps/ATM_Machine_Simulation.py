'''

In this project, I am building an ATM Machine Simulation without using loops. 
It is a simple version, so no edge cases will be covered.

'''
# This is correct pin
correct_pin = 1234

# This is users initial_balance
initial_balance = 1000


# Showig options
def options():
    print("1. Check Balance")
    print("2. Cash Deposit")
    print("3. Cash Withdraw")
    print("4. Exit")

# Taking pin
pin = int(input("Enter pin :").strip())

if pin == 1234:
    print("Correct pin")

    options()  # Calling function to show options 

    
    choose = input("Choose option [1/2/3/4] :").strip()

    # Condition for option 1

    if choose == "1":
     print(f"Your balance is :${initial_balance}")
    
    # Condition for option 2

    elif choose == "2":

        deposite = float(input("Enter the amount :$").strip())
        initial_balance += deposite
        
        print('----------------------')
        print("Deposite successful")
        print(f"Your current balance is :${initial_balance}")
        print('-----------------------')

    # Condition for option 3

    elif choose == "3":

        print(f"Your Balance is :${initial_balance}")
        withdraw = float(input("Enter amount :$").strip())

        if withdraw > initial_balance:
            print("Insufficient Balance")

        else:
            initial_balance -= withdraw
            print('-------------------')
            print("Withdraw Successful")
            print(f"Remaining balance is :${initial_balance}")
            print('-------------------')
        

    # Condition for option 4

    if choose == "4":
        print("Thank you for coming")

else:
    print("Wrong pin")
