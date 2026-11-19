p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = int(input("Enter time in years: "))

amount = p * (1 + r / 100) ** t
ci = amount - p

print("Total Amount:", amount)
print("Compound Interest:", ci)