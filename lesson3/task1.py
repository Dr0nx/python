def division(a, b):
    return a / b


number1 = int(input('Введите число a: '))
number2 = int(input('Введите число b: '))

try:
    result = division(number1, number2)
    print(result)
except ZeroDivisionError:
    print('Денеие на ноль!')
