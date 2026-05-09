#  Python basic Calculator

operator = input("Enter the operators :(+ - * /) ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

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
    if num2 == 0:
        print("Error!! Cannot divide by zero")
    else:
        result = num1 / num2
        print(round(result, 3))
else:
    print(f"The '{operator}' is not a valid operator.")

exit(2)
