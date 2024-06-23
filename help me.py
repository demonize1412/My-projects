num1 = int(input("введите четное число больше 10: "))
if 10 < num1 and num1 % 2 == 0:
    print("правильно!")
elif num1 < 10 or num1 % 2 != 0:
    print("не правильно")
if num1 < 10:
    print("вы ввели:", num1, "это меньше 10.")
if num1 > 10 and num1 % 2 == 0:
    print("вы молодец!")
