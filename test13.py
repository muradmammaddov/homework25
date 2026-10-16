age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
loan = float(input("Enter your loan amount: "))
if age < 0 or salary < 0 or loan <= 0:
    print("Rejected")
elif age < 18 or salary < 500 or loan > 10 * salary:
    print("Rejected")
else:
    print("Approved")