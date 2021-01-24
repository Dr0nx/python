counter = 0
added_list = []

while True:
    if counter == 0:
        result = input('Введите элементы. Клавиша Enter завершает ввод: ')
    else:
        result = input('Введите еще элементы: ')

    if result == '':
        break

    added_list.append(result)

    if counter % 2:
        temp = added_list[counter]  # print('Четное')
        added_list[counter] = added_list[counter - 1]
        added_list[counter - 1] = temp

    counter += 1

print('Измененные элементы:', added_list)
