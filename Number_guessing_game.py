'''

In this project i am gonna make a number guessing game.
python will choose a number and user have to guess it.

'''

# Using library
import random

number = random.randint(1,10) # Giving a range to choose number


# This is for UX

print("\n" + "=" *37)
print("Welcome to the number guessing game")
print("=" *37)

# Attempt count 
attempt = 0

# Loop
while True:

# Taking guess from the user

    guess_input = input("Guess the number : ").strip()

    try:
        guess = int(guess_input) # Trying to convert it into interger
        attempt += 1 # Counting attempts

# If the guess is correct

        if guess == number:
            print(f"\n Choosed number :{number}")
            print(f"\n Your guess was :{guess}")
            print(f"\n Total attempt :{attempt}")
            print("\n Congratulation Your guess is correct 🎉")
            
            break

# If the guess is bigger than the actual number

        elif guess > number:
            print("\nOh, bro your guess is high 📈")
            continue
# If the guess is smaller than tha actual number

        elif guess < number:
            print("\nOh, bro your guess is low 📉")
            continue

        else:
            print("plz try again")


 # If try will fail then expcept will handel it
    except ValueError: 
        print("\nEnter only integers") 