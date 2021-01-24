revenue = float(input('Введите значение выручки: '))
cost = float(input('Введите значение издержек: '))

if revenue > cost:
    employees = int(input('Введите количество сотрудников: '))
    profit = revenue - cost
    print('Фирма работает с прибылью')
    print(f"Рентабельность выручки составила {(profit / revenue) * 100}")
    print(f"Прибыль в расчете на одного сотрудника сотавила {profit / employees:}")
elif revenue < cost:
    print('Фирма работает в убыток')
else:
    print('Фирма работает в 0')

