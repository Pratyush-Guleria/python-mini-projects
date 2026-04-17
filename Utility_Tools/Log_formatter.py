messy_input = " error: 404 - connection failed "

messy = messy_input.strip().replace("error", "[SYSTEM FAILURE]").upper()

print(f"The output of  error: 404 - connection failed is : {messy}")