"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
from typing import List
import json

with open("text71.txt", "r") as f_obj:
    lines = f_obj.read().splitlines()
    revenue = 0
    quantity = 0
    for el in lines:
        line = el.split()
        line[2] = int(line[2])
        line[3] = int(line[3])
        profit = line[2] - line[3]
        if profit > 0:
            revenue = revenue + line[2]
            quantity += 1
            print(f'Прибыль по компании {line[0]} составила {profit} р.')
    try:
        average = revenue / quantity
        print(f'Средняя прибыль по компаниям составила: {average:.2f} р.')
    except ZeroDivisionError:
        print('Работа в ноль.')

with open("text71.txt", "r") as f_obj:
    list1 = []
    list2 = []
    list3 = []
    lines = f_obj.read().splitlines()
    for el in lines:
        line = el.split()
        line[2] = int(line[2])
        line[3] = int(line[3])
        profit = line[2] - line[3]
        if profit > 0:
            list1.append(line[0])
            list1.append(line[2])
        else:
            list2.append(line[0])
            list2.append(line[3])
    average = 0
    revenue = 0
    quantity = 0
    for i, el in enumerate(list1):
        if i % 2 == 1:
            revenue = revenue + int(el)
            quantity += 1
    try:
        average = revenue / quantity
    except ZeroDivisionError:
        print('Деление на ноль.')
    dict1 = {list1[i]: list1[i + 1] for i in range(0, len(list1), 2)}
    dict2 = {list2[i]: list2[i + 1] for i in range(0, len(list2), 2)}
    list3.append(dict1)
    list3.append({"average_profit": average})
    list3.append(dict2)

with open("text71.json", "w") as write_f:
    json.dump(list3, write_f)
    print(f'json-объект: {list3}')
