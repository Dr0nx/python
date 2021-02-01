"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто
из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины доход
сотрудников.
"""

with open("text3.txt", "r") as f_obj:
    text = f_obj.read().splitlines()
    average = 0
    for index, el in enumerate(text):
        split_line = text[index].split()
        salary = int(split_line[2])
        if salary < 20000:
            first_last = split_line[0] + ' ' + split_line[1]
            print(f'{first_last} получает менее 20000 т. р. ({salary})')
        average += salary
    print(f'Средняя величина дохода сотрудников: {average / index + 1:.2f} т.р.')
