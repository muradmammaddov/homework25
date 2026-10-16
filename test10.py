withdrawal = int(input())
balance = 1000
if withdrawal <=0:
    print("Invalid amount")
elif withdrawal > balance:
    print("Unsufficient balance")
else:
    print(balance - withdrawal)
