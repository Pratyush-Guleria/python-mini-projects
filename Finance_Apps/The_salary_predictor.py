
'''
NOTE: This project is just build for practice pourposes only this project does not predict something in real life.
In this project i am gonna build a program that Predict the salary.
'''

# This is for UX
print("--- FUTURE SALARY PREDICTOR ---")

def predict_future(commits,skill):

    try:
        c = int(commits)
        s = int(skill)

        if c > 500 and s > 8:
            return ("Package: 1 Crore")
	  
        elif c >200 and s > 5:
            return ("Package: 25LPA - 40LPA")
	   
        elif c > 100:
            return("Package: 10LPA")

        else:
            return ("Keep grinding bro")
    except ValueError:
            return ("Please enter something")

    except Exception as e:
            return (f"This is is the Error: {e}")

commit_input = input("Enter how much commit do you have: ").strip()
skill_input = input("Enter the level of skill [1 - 10]: ").strip()

result = predict_future(commit_input,skill_input)

print(result)
