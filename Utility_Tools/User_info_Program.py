"""
User Identification and Age Classification System
Purpose: To collect user details, assign titles based on gender, 
         and categorize them by age group with error handling. 
"""


#--- Step 1 : User Name Input & Validation ---

while True :

    name = input("What's your name :").strip().title()

    if not name:
        print("You didn't enter your name")
        continue

    else:
        print(f"Hello : {name}")
        break

#---Step 2 : User Gender input and Title assignment ---

while True:
        
        gender_input = input("what's your gender (M/F) :").strip().capitalize()

        
        if gender_input =="M":
            gender = "Mr."
            break

        elif gender_input =="F":
            gender = "Ms."
            break
        
        else:
            print("Plz enter M or F only")
            continue

# --- Step 3 : User Age input and Classification

while True :

    age_input = input("What's your age :").strip()

    try:
        age = int(age_input)

        if age < 0:
            print(f"Sorry : {gender} {name}, You are not born yet")
            continue

        elif age < 18:
            print(f"Category: Minor | User: {gender} {name}")
            break
 
        elif age >=60:
            print(f"Category: Senior Citizen | User: {gender} {name}")
            break


        else:
            print(f"Category: Adult | User: {gender} {name}")
            break

    except ValueError:
        print("Plz enter integers only")