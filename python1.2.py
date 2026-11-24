# Same object
a = [10, 20, 30]
b = a

# Different objects
x = [10, 20, 30]
y = [10, 20, 30]

# Identity operators
print("a is b:", a is b)
print("x is y:", x is y)

print("a is not b:", a is not b)
print("x is not y:", x is not y)