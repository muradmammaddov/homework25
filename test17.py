order_total = int(input("Enter order total: "))
membership = input("Do u have a membership kiddo?: ")
if order_total < 0 or (membership != "yes" or membership != "no"):
    print("Rejected")
else:
    delivery_fee = 5 if (membership != "yes" and order_total < 50) else 0
    print(delivery_fee)
    print(order_total + delivery_fee)
