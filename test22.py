phone_number = input("Enter phone number: ")
if phone_number == "":
    print("Invalid phone number")
elif len(phone_number) != 10:
    print("Invalid phone number")
elif phone_number.isdecimal() == False:
    print("Invalid phone number")
else:
    prefix = phone_number[:3]
    match prefix:
        case "050":
            print("Valid")
        case "051":
            print("Valid")
        case "055":
            print("Valid")
        case "070":
            print("Valid")
        case "077":
            print("Valid")
        case "099":
            print("Valid")
        case _:
            print("Invalid phone number")


