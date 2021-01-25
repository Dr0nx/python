def division(a, b):
    return a / b


try:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    result = division(number1, number2)
    print(result)
except ZeroDivisionError:
    print('Деление на ноль!')
except ValueError:
    print("Небходимо число!")
