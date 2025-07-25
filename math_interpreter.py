#prompt the user for an arithmetic expression
result = 0
expression = input("Expression: ")
#check the math operation and execute it
parts = expression.split(" ")
operation = parts[1]
x = float(parts[0])
y = float(parts[2])

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
