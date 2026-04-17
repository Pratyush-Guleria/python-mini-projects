password = input("What's your password :").strip()

password_len = len(password)
print(f"Lenght of your password :{password_len}")
if password_len >= 3:
    result = password[0] + "*" *(len(password) - 2) + password[-1]
    print(result)

else:
    print("Your password is too short")