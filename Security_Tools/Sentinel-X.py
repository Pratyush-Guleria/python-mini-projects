"""

In this i am gonna build a project and the name of the project is Sentinel-X.
This project rejects the trash data and validate the clean data.

"""

# This is for UX

print("\n--- SENTINEL-X: SYSTEM ONLINE ---")

# Here are some important things

total_scanned = 0
error_count = 0
success_count = 0


# Here is a loop

while True:

    data = input("Enter Data Packet (or EXIT) :").strip()

# If user will EXIT

    if data.upper() =="EXIT":
        break

# If user will just hit enter

    elif data =="":
        print("Plz enter something")
        continue

    total_scanned +=1


# If the Packet is too short 

    if len(data) < 3:
        print(f"Packet #{total_scanned}: REJECTED ❌ (Reason: too short)")

        error_count += 1
        

# If the Packet has security issues

    elif not data.isalnum():
        print(f"Packet #{total_scanned}: REJECTED ❌ (Reason: Security Risk)")
        error_count +=1

# After passing all the conditions

    else:
        success_count +=1
        print(f"Packet #{total_scanned}: VALIDATED ✅ -> Processed: {data.upper()}")


# 4. Final Report Logic
print("\n" + "="*40)
print("         FINAL INTEGRITY REPORT         ")
print("="*40)
print(f"Total Packets Scanned : {total_scanned}")
print(f"Successful Ingests    : {success_count}")
print(f"Errors Blocked        : {error_count}")
print("="*40)