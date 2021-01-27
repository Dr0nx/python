i = 0
summa = 0
result = 0

while True:
    if result:
        break
    string_to_int = input("Введите строку чисел, разделенных пробелом.\n"
                          "При нажатии на Enter выводиться сумма чилел. ")
    while True:
        if not len(string_to_int):
            break
        int_number = string_to_int.split()
        if not int_number[-1].isnumeric():
            result = 1
            int_number.reverse()
            del int_number[0]
        int_number = list(map(int, int_number))
        for each in int_number:
            summa = summa + each
        print(summa)
        break

