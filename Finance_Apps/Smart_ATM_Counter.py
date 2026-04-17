correct_pin = 123
attempt = 0 
balance = 500
while True:

    user_input = input("Enter pin :").strip()

    if user_input =="":
        print("Sorry you didn't entered anything")
        continue 
    
    if not user_input.isdigit():
        print("Please enter only number (0-9)")
        continue

    pin = int(user_input)
    if pin == correct_pin:
        print ("Correct pin")

        check = input("Do you want to check your balance (Y/N) :").upper()

        if check =="Y":
            print(f"Your balance is :${balance}")

            break

        elif check =="N":
            print("Ok thanks")

            break

        else:
            print("Sorry invalid option, exiting")

            break

    else:
        attempt +=1
        print(f"Wrong pin entered, You have {3 - attempt} attempt left")
        if attempt ==3:
            print("Account blocked")
            break