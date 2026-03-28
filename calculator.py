operator = input("Choose one operator + - * /")
num1 = float(input("enter num1"))
num2 = float(input("enter num2"))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print("Your request is invalid!")
    