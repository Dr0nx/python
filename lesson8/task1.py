"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

integer = []


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date_class(cls, date):
        string = date.split('-')
        for el in string:
            integer.append(int(el))
        return integer

    @staticmethod
    def get_date_static():
        if integer[1] == 2:
            border = 28
        elif integer[1] in [4, 6, 9, 11]:
            border = 30
        elif integer[1] in [1, 3, 5, 7, 8, 10, 12]:
            border = 31
        else:
            return 'Неверный формат месяца!'

        if 1 <= integer[0] <= border:
            day = integer[0]
        else:
            return 'Неверный формат дня!'

        if 1 <= integer[1] <= 12:
            month = integer[1]
        else:
            return 'Неверный формат месяца!'

        if 1970 <= integer[2] <= 2021:
            year = integer[2]
        else:
            return 'Неверный формат года! (Счет с 01.01.1970 года.)'

        return f'Дата {day}.{month}.{year} верна.'


Date.get_date_class('28-02-1977')
print(Date.get_date_static())
