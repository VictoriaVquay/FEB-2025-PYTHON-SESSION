# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation and print the result
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} {operation} {num2} = {result}")
else:
    print("Error: Invalid operation.")

# If the operation was valid and not division by zero, print the result
if operation in ('+', '-', '*') or (operation == '/' and num2 != 0):
    print(f"{num1} {operation} {num2} = {result}")
