operator = input("Enter an operator: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
elif operator == "%":
    result = num1 % num2
    print(round(result, 3))
else:
    print(f"{operator} is invalid")