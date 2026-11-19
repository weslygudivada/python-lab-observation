a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
else:
    print("Division, Floor Division and Modulus are not possible")

print("Exponentiation:", a ** b)