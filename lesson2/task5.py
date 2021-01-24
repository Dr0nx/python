my_list = [89, 55, 55, 47, 5, 3, 3, 2]
count = 0

result = int(input('Введите число: '))
for index, item in enumerate(my_list):
    if result == item:
        my_list.insert(index, item)
        break
    elif result > item:
        my_list.insert(index, result)
        break
    else:
        if count == 1:
            my_list.append(1)
            break
        else:
            while count < result:
                if count == result:
                    my_list.insert(count, result)
                    break
                count += 1

print('Результат:', ', '.join(map(str, my_list)))
