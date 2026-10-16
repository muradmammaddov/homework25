score = int(input("Enter score: "))

if score < 0:
    print("Invalid score")
elif score <= 50:
    print("F")
elif score <= 60:
    print("E")
elif score <= 70:
    print("D")
elif score <= 80:
    print("C")
elif score <= 90:
    print("B")
elif score <= 100:
    print("A")
else:
    print("Invalid score")