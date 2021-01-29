import random

list1 = [random.randint(0, 9) for el in range(0, 10)]
list2 = [el for el in list1 if list1.count(el) == 1]

print(f'Исходный список: {list1}\nРезультат:       {list2}')