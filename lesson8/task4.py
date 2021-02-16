"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class Warehouse:

    def __init__(self):
        self._dict = {}

    def to_add(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract_from(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

    @property
    def dict(self):
        return self._dict


class OfficeEquipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'


class Printer(OfficeEquipment):
    def __init__(self, name, price, quantity, cartridge_name):
        super().__init__(name, price, quantity)
        self.cartridge_name = cartridge_name

    def __repr__(self):
        return f'Принтер: {self.name}, Цена: {self.price} р, ' \
               f'Количество: {self.quantity} шт, Картридж: {self.cartridge_name}'

    def action(self):
        return f'Печатаю на {self.name} используя картридж {self.cartridge_name}'


class Scaner(OfficeEquipment):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f'{self.name}, {self.price}, {self.quantity}'

    def action(self):
        return f'Сканирую на {self.name}'


class Xerox(OfficeEquipment):
    def __init__(self, name, price, quantity, cartridge2_name):
        super().__init__(name, price, quantity)
        self.cartridge2_name = cartridge2_name

    def __repr__(self):
        return f'{self.name}, {self.price}, {self.quantity}, {self.cartridge2_name}'

    def action(self):
        return f'Делаю ксерокс {self.name} используя картридж {self.cartridge2_name}'


warehouse = Warehouse()
printer = Printer('Canon', 5000, 2, 'canon заправка')
warehouse.to_add(printer)
printer = Printer('HP', 10000, 1, 'hp заправка')
warehouse.to_add(printer)
scaner = Scaner('Canon', 5000, 2)
warehouse.to_add(scaner)
scaner = Scaner('HP', 2000, 1)
warehouse.to_add(scaner)
xerox = Xerox('Canon', 15000, 1, 'xerox заправка')
warehouse.to_add(xerox)
print(warehouse.dict)
warehouse.extract_from('Printer')
print(warehouse.dict)
print(printer.action())
print(scaner.action())
print(xerox.action())