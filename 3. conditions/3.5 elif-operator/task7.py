# Калькулятор своими руками

num1, num2, operator = float(input()), float(input()), input()

if operator not in "+-*/" or (operator == "/" and (num1 == 0 or num2 == 0)): print("Неизвестно")
elif operator == "+": print(num1 + num2)
elif operator == "-": print(num1 - num2)
elif operator == "*": print(num1 * num2)
elif operator == "/": print(num1 / num2)