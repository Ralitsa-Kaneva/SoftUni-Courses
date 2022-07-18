def calculator(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return int(num1 / num2)
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2


command = input()
number1 = int(input())
number2 = int(input())

print(calculator(command, number1, number2))
