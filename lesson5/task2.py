"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества
слов в каждой строке.
"""

with open("text2.txt", "r") as f_obj:
    number_of_lines = 0
    for line in f_obj:
        number_of_lines += 1
    print(f'Количество строк: {number_of_lines}\n')

with open('text2.txt') as f_obj:
    lines = f_obj.readlines()
    for index, value in enumerate(lines):
        number_of_words = len(value.split())
        print(f'В строке {index + 1}  слов: {number_of_words} \t{lines[index]}', end='')
