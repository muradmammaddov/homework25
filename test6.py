a = float(input("First number: "))
b = float(input("Second number: "))
c = input("Operation: ")
#+, -, *, /, %, **, //
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b == 0:
        print("Invalid operation")
    else:
        print(a / b)
elif c == "%":
    if b == 0:
        print("Invalid operation")
    else:
        print(a % b)
elif c == "**":
    if a == 0 and b < 0:
        print("Invalid operation")
    elif a < 0 and b != int(b):
        print("Invalid operation")
    else:
        print(a ** b)
elif c == "//":
    if b == 0:
        print("Invalid operation")
    else:
        print(a // b)

