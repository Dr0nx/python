def my_func(arg1, arg2, arg3):
    number1 = arg1 + arg2
    number2 = arg1 + arg3
    number3 = arg2 + arg3

    if (number1 >= number2) and (number1 >= number3):
        return number1
    elif (number2 >= number1) and (number2 >= number3):
        return number2
    else:
        return number3

try:
    result1 = int(input("Введите первый позиционный аргумент: "))
    result2 = int(input("Введите второй позиционный аргумент: "))
    result3 = int(input("Введите третий позиционный аргумент: "))
    print("Сумма наибольших двух аргументов:", my_func(result1, result2, result3))
except ValueError:
    print("Введите только число!")
