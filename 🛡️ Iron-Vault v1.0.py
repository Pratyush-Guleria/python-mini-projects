# Here is a master pin 
master_pin = 129

# This is for UX
print("\n")
print("--- 🛡️ IRON-VAULT v1.0 ACCESS ---")
print("\n")

# The action menu

def action_menu():
    '''
    This will show menu to the user
    '''
    print("\n" + "-" * 30)

    print("1️⃣ Add New Secret✍️ :")

    print("2️⃣ View All Secret 📖 :")
    
    print("3️⃣ Exit & Lock Value 🔒 :")

    print("-" * 30)

# Loop

while True:

                # Error Handling 
    try :
        user_input = int(input("🔒 Enter Master Pin :").strip())

    except ValueError:
        print("Integers are allowed only")
        continue

    else:
        print("Input Successful")
        
                
                # Checking the master pin

    if user_input == master_pin:
        print("✅ ACCESS GRANTED! Welcome back")
        break 

    else:
         print("Wrong pin Entered")
         continue


# Dictionary
value = {}

# Loop
while True: 

    # Calling the function 

    action_menu()

    # Error handling
    try :

        select_options = int(input("Enter options number (1/2/3) :").strip())

    except ValueError:
        print("Integers are allowed only")
        continue

    # If user will try to input invalide option

    if select_options > 3 or select_options <= 0:

        print("Invalid option, Please Choose between 1, 2 or 3")
        continue

    # If user will choose option 1

    if select_options == 1:

        print("\n--- ✍️ ADD NEW SECRET ---")

        key = input("Enter Secret Name (e.g. Gmail) :").strip()
        secret_data = input(f"Enter secret for {key} : ").strip()

        value[key] = secret_data
        print(f"✅ {key} has been locked in the vault")

    # If user will choose option 2

    elif select_options == 2:

        if not value :
            print("Your value is empty")

        else:
            print("\n--- 📂 YOUR VAULT ---")

        for name,secret in value.items():
                print(f"🔑 {name}: {secret}")

    # If user will choose option 3

    if select_options == 3:
        print("Exit & Lock Value Successfully 🔒")
        break 

    elif select_options > 3 or select_options < 0:

        print("Invalid option, Please try again")
        continue