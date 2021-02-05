"""
Реализовать базовый класс Worker (работник).
- определить атрибуты: name, surname, position (должность), income (доход);
- последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus};
- создать класс Position (должность) на базе класса Worker;
- в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
(get_total_income);
- проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров.
"""


class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        self._income['wage'] = wage
        self._income['bonus'] = bonus
        return self._income['wage'] + self._income['bonus']


name1 = input('Введите имя: ')
surname1 = input('Введите фамилию: ')
position1 = input('Введите должность: ')
try:
    wage = int(input('Введите оклад: '))
    bonus = input('Введите бонус: ')
    if not bonus.isdigit():
        bonus = 0
except ValueError:
    print('Небходимо ввести число!')
    exit(1)

instance = Position(name1, surname1, position1)
print(f'Сотрудник {instance.get_full_name()} получает оклад с учетом премии {instance.get_total_income()} р.')
