# Guardian Pattern Example
# Prevents division by zero errors

x = 10
y = 2

# Guardian condition
if y != 0 and (x / y) > 2:
    print("Result is greater than 2")
else:
    print("Condition not met")