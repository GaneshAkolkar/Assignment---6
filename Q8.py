a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    print("The quadratic equation has two real and distinct roots.")
elif discriminant == 0:
    print("The quadratic equation has real and equal roots.")
else:
    print("The quadratic equation has imaginary roots.")
