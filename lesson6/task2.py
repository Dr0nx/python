"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу
метода.
Например: 20м * 5000м * 25кг * 5см = 125003т.
"""


class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def method_for_calc(self, thickness, weight):
        return self._length * self._width * thickness * weight


road = Road(20, 5000)
weight = road.method_for_calc(25, 5) / 1000
print(f'Масса асфальта: {weight:.0f} тонн')
