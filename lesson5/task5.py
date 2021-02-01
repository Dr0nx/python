"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("text5.txt", "w") as f_obj:
    numbers = input('Введите числа через пробел: ')
    f_obj.write(numbers)
    my_list = numbers.split()
    summa = 0
    for el in my_list:
        try:
            summa += int(el)
        except ValueError:
            print('Введено не число!')
            f_obj.seek(0)
            f_obj.truncate()
            exit(1)
    print(f'Сумма чисел: {summa}')
