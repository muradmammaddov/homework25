stored_pin = "0427"
attempt = input("Please enter your attempt number: ")
if attempt == "":
    print("Pin is required")
elif len(attempt) != 4:
    print("PIN must have 4 digits")
elif attempt.isdecimal() == False:
    print("Digits only")
elif attempt == stored_pin:
    print("Access granted")
else:
    print("Invalid")