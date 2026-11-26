n = int(input("Enter a number (1-100): "))

flag = 0

if n == 1:
    print("Not a Prime Number")
else:
    for i in range(2, n):
        if n % i == 0:
            flag = 1
            break

    if flag == 1:
        print("Not a Prime Number")
    elif flag == 0:
        print("Prime Number")