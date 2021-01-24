counter = 0
print('Список элементов:')
another_list = [15, 'Hi!', 45.12, ('red', 'green'), {1, 4, 2}, {'key_1': 'val_1', 'key_2': 'val_2'}, False]
for element in another_list:
    print(f'{type(element)} {another_list[counter]}')
    counter += 1
