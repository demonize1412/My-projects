print('Программа для высчитывания математической прогрессии')
num1 = int(input("напишите число:"))
num2 = int(input('введите второе число:'))
while num1 > 0:
    num1 -= num2
    if num1 != 0:
        print(num1)
    else:
        continue
print('Ответ:', num1 + num2, 'или', num1)
