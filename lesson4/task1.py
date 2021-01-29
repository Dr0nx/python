def payroll():
    try:
        production_in_hour = float(input('Введите выработку в часах: '))
        rate_per_hour = int(input('Ставка в час: '))
        premium = int(input('Премия: '))
    except ValueError:
        print('Введено не число')
    else:
        print(f'Расчет заработной платы составил: {production_in_hour * rate_per_hour + premium}')


payroll()
