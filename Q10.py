a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b and a > c:
    print(a, "is the greatest number")
elif b > a and b > c:
    print(b, "is the greatest number")
elif c > a and c > b:
    print(c, "is the greatest number")
else:
    print("All numbers are equal")
