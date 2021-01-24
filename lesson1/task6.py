day = int(input('Введите значение первого дня в километрах: '))
last_day = int(input('Введите значение в километрах, которое нужно достичь (как минимум): '))
count = 1

while True:
    print(f'{count}-й день: {day:.2f}')
    day = day * 10 / 100 + day
    count += 1
    if day > last_day:
        print(f'{count}-й день: {day:.2f}')
        break

print(f'На {count}-й день спортсмен достиг результата — не менее {last_day} км.')
