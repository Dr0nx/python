count = 1
year = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
seasons = ['зима', 'весна', 'лето', 'осень']
seasons2 = {1: 'зима', 2: 'зима', 3: 'весна',
            4: 'весна', 5: 'весна', 6: 'лето',
            7: 'лето', 8: 'лето', 9: 'осень',
            10: 'осень', 11: 'осень', 12: 'зима'}

while True:
    if month <= 0 or month > 12:
        print('Нужно ввести число в диапазоне от 1 до 12. Попробуйте еще раз: ')
        month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
    else:
        break

# через list
while count <= 12:
    if month == count:
        if count <= 2:
            season = seasons[0]
            break
        elif 3 <= count <= 5:
            season = seasons[1]
            break
        elif 6 <= count <= 8:
            season = seasons[2]
            break
        elif 9 <= count <= 11:
            season = seasons[3]
            break
        else:
            season = seasons[0]
            break
    count += 1

print('Это будет', season, '(через list)')

# Через dict
for key in seasons2:
    if key == month:
        break

print('Это будет', seasons2[key], '(через dict)')
