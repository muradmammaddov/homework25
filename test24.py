product_code = input("Enter product code: ")
quantity = input("Enter quantity: ")
coupon_code = input("Enter coupon code: ")
delivery_code = input("Enter delivery code: ")
match product_code:
    case "K":
        price = 40
    case "M":
        price = 20
    case "H":
        price = 60
    case _:
        print("Invalid product code")

if quantity.isascii() == False or quantity.isdecimal() == False:
    print("Quantity must contain only digits")
elif not(1<=int(quantity)<=5):
    print("must be between 1 and 5")
else:
    quantity = int(quantity)
    



