int_var = input('Введите число: ')

if int_var.isdecimal():
    print(int_var)
else:
    print('Нужно было ввести число!')

str_var = input('Введите строку: ')

if str_var.isalpha():
    print(str_var)
else:
    print('Нужно было ввести строку!')
