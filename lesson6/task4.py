"""
Реализуйте базовый класс Car.

- у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
- добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
- для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
"""

from random import randint
from random import choice

excess = [60, 40]
speed1 = 0
color1 = ['красного', 'серого', 'черного', 'белого']
name1 = ['Мерседес', 'БМВ', 'Ауди', 'ВАЗ']


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def __str__(self):
        if self.go():
            return (f'Автомобиль {self.color} {self.name} едет со скоростью {self.show_speed()} км/ч '
                    f'на {self.turn(choice(["север", "запад", "юг", "восток"]))}.')
        else:
            return f'Автомобиль {self.name} {self.color} цвета стоит.'

    def go(self):
        return self.speed >= 1

    def stop(self):
        return self.speed == 0

    @staticmethod
    def turn(direction):
        return direction

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def __str__(self):
        if self.go() and self.speed <= excess[0]:
            return (f'Автомобиль {self.color} {self.name} едет со скоростью {self.show_speed()} км/ч '
                    f'на {self.turn(choice(["север", "запад", "юг", "восток"]))}.')
        elif self.speed > excess[0]:
            return (f'Скорость {self.color} автомобиля {self.name} больше на {excess[0]} км/ч! Превышение '
                    f'на {self.show_speed() - excess[0]} км/ч. ({self.show_speed()} км/ч)')
        else:
            return f'Автомобиль {self.name} {self.color} цвета стоит.'


class SportCar(Car):
    pass


class WorkCar(Car):

    def __str__(self):
        if self.go() and self.speed <= excess[1]:
            return (f'Автомобиль {self.color} {self.name} едет со скоростью {self.show_speed()} км/ч '
                    f'на {self.turn(choice(["север", "запад", "юг", "восток"]))}.')
        elif self.speed > excess[1]:
            return (f'Скорость {self.color} автомобиля {self.name} больше на {excess[1]} км/ч! Превышение '
                    f'на {self.show_speed() - excess[1]} км/ч. ({self.show_speed()} км/ч)')
        else:
            return f'Автомобиль {self.name} {self.color} цвета стоит.'


class PoliceCar(Car):
    pass


car = Car(randint(0, 120), color1[randint(0, 3)], name1[randint(0, 3)], is_police=False)
print(car)
town = TownCar(randint(0, 120), color1[randint(0, 3)], name1[randint(0, 3)], is_police=False)
print(town)
work = WorkCar(randint(0, 120), color1[randint(0, 3)], name1[randint(0, 3)], is_police=False)
print(work)
sport = SportCar(randint(0, 120), color1[randint(0, 3)], name1[randint(0, 3)], is_police=False)
print(sport)
police = PoliceCar(randint(0, 120), color1[randint(0, 3)], name1[randint(0, 3)], is_police=False)
print(police)
