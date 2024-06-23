def print_hello():
    print('Здравствуйте, это калькулятор написанный на python')


print_hello()
while True:
    num1 = int(input("введите 1 число: "))  # we enter the first number for calculations
    zn = input("введите операцию: ")  # introducing a mathematical action
    num2 = int(input("введите 2 число: "))  # we enter the second number for calculations
    if zn == "+":
        print("ваш ответ:", num1 + num2)
    elif zn == "-":
        print("ваш ответ:", num1 - num2)
    elif zn == "*":
        print("ваш ответ:", num1 * num2)
    elif zn == "/":
        print("ваш ответ:", num1 / num2)
    elif zn == "**":
        print("ваш ответ:", num1 ** num2)
    elif zn == ("//"):
        print("ваш ответ:", num1 // num2)
