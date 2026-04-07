password = input("What's your password :").strip()

result = password[0] + "*" *(len(password) - 2) + password[-1]

print(result)