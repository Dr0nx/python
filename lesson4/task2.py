list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list2 = [el for index, el in enumerate(list1) if list1[index - 1] < list1[index] and index != 0]
print(f'Исходный список: {list1}\nРезультат: {list2}')
