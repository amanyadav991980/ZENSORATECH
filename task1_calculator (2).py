# Task 1: Basic Arithmetic Calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
    print(f"The result is: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"The result is: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"The result is: {result}")
elif operator == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        result = num1 / num2
        print(f"The result is: {result}")
else:
    print("Invalid operator. Please use +, -, *, or /")
