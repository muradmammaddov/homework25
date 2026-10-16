balance = 1000
storedBalance = "0427"
amount = input("Enter an amount: ")
pin = input("Enter a pin: ")
if len(pin) != 4:
    print("Pin must contain four digits")
elif pin.isascii() == False or pin.isdecimal() == False:
    print("Digits only")
elif amount.isascii() == False or amount.isdecimal() == False:
    print("Amount must only contain digits")
else:
    amount = int(amount)
    if not(10<=amount<=500):
        print("Amount must be between 10 and 500")
    elif amount % 10 == 1:
        print("Opss...Banknot rule")
    fee = 0 if amount <= 200 else 2
    if amount + fee > balance:
        print("Balance exceeds your account")
    else:
        print("Withdrawal amount ", amount)
        print("Fee", fee)
        print("New balance", balance - (amount + fee))
