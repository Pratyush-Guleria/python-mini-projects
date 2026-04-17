name = input("What is your name :").strip().upper()

college = input("What is your collage name :").strip().upper()

skill = input("Which skill do you have :").strip().upper()

DOB = int(input("In which year you born :").strip())

age = 2026 - DOB

if age >= 18:
     Professional_status = "You are eligible for Internships"

else :
     Professional_status = "Junior Student"

print("-------------------------")
print(f"Student ID: {name}")
print(f"AGE: {age}")
print(f"COLLEGE: {college}")
print(f"SKILL: {skill}")
print(f"Professional Status: {Professional_status}")
print("-------------------------")