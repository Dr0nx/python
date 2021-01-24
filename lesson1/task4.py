var = int(input('Введите целое положительное число: '))
number = 0
max_number = 0

while var > 0:
    var = var // 10
    number = var % 10
    if number > max_number:
        max_number = number

print("Самая большая цифра:", max_number)
