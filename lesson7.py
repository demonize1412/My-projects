# name = input('введите свое имя:')
# def print_hello(name):
#   print('hello', name)
def bb(num1, num2):
    result = num1 + num2
    return result


ch = 52
ch2 = 55
# print(bb(ch, ch2))
res = bb(ch, ch2)
if res > 100:
    print(res, 'ты крут')
else:
    print(res, 'buy, buy')
