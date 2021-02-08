"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from random import randint
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def my_method(self):
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    def get_clothes(self):
        return self.V / 6.5 + 0.5

    def my_method(self):
        print('Проверка работы метода my_method(self) внутри coat')


class Costume(Clothes):
    def __init__(self, H):
        self.H = H

    def get_clothes(self):
        return 2 * self.H + 0.3

    def my_method(self):
        print('Проверка работы метода my_method(self) внутри costume')


class Test:
    def __init__(self, test):
        self.test = test

    @property
    def my_method(self):
        return f'Параметры, переданные в класс: {self.test} способ test.my_method'


x = 5
size = [randint(88, 120) for z in range(x)]
growth = [randint(158, 182) for z1 in range(x)]

print(f'Для двух классов Coat и Costume будет создано по {x} экземпляров c случайными данными.')
index, total_count = 0, 0
while index < len(size):
    coat = Coat(size[index])
    costume = Costume(growth[index])
    tolal_coat = coat.get_clothes() / 10
    total_costume = costume.get_clothes() / 100
    print(f'Расход ткани для пальто {index + 1} составил {tolal_coat:.2f} метра (V/6.5 + 0.5), '
          f'для костюма {index + 1} - {total_costume:.2f} метра (2*H + 0.3)')
    total_count += tolal_coat + total_costume
    index += 1
print(f'Общий подсчет расхода ткани составил: {total_count:.2f}')
coat.my_method()
costume.my_method()
test = Test('123')
print(test.my_method)
