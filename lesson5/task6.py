"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

with open("text6.txt", "r") as f_obj:
    my_list = f_obj.read().splitlines()
    my_dict = {}
    for i, el in enumerate(my_list):
        split_line = my_list[i].split()
        item = split_line[0]
        item = item[:-1]
        count1 = 1
        count2 = 1
        summa = 0
        while count1 <= 3:
            while count2 <= 3:
                amount_list = split_line[count2].split('(')
                amount = amount_list[0]
                if amount == '-':
                    amount = 0
                summa += int(amount)
                count2 += 1
            my_dict.update({item: summa})
            count1 += 1

    print(f'Результирующий словарь: {my_dict}')
