a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c= input("Enter an operation (+, -, *, /): ")

if c == '+':
    print(f"Result: {a + b}")
elif c == '-':
    print(f"Result: {a - b}")
elif c == '*':
    print(f"Result: {a * b}")
elif cn == '/':
    if b != 0:
        print(f"Result: {a / 2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")
