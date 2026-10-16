a = int(input())
b = int(input())
c = int(input())
if a + b > c:
    if a + c > b:
        if b + c > a:
            if a == b == c:
                print("Equilateral")
            elif a == b or b == c or a == c:
                print("Isosceles")
            else:
                print("Scalene")
else:
    print("Triangle cannot be created")