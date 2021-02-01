"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

my_list_russian = ['один', 'два', 'три', 'черыре']
with open("text41.txt", "r") as f_obj:
    with open("text42.txt", "w", encoding='utf-8') as f_obj2:
        input_data = f_obj.read().splitlines()
        for index, el in enumerate(input_data):
            split_line = input_data[index].split()
            out_data = f'{my_list_russian[index]} {split_line[1]} {split_line[2]}\n'
            f_obj2.writelines(out_data)
print('Новый блок строк в файле text42.txt.')
