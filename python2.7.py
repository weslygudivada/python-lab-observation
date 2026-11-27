n = int(input("How many numbers? "))

largest = float(input("Enter a number: "))

for i in range(n - 1):
    num = float(input("Enter a number: "))

    if num > largest:
        largest = num

print("Largest number =", largest)
