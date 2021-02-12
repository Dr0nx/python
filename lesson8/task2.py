"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


try:
    number1 = int(input('Введите первое целое число: '))
    number2 = int(input('Введите второе целое число: '))
    if number2 == 0:
        raise MyZeroDivisionError(number1, number2)
except MyZeroDivisionError:
    print('Произошло деление на ноль!')
except ValueError:
    print('Допустимы только целые числа!')
else:
    print(f'Целочисленное деление {number1} / {number2}: {(number1 / number2):.2f}')
