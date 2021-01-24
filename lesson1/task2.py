seconds_to_time = int(input('Введите время в секундах: '))

seconds = seconds_to_time % 60
minutes = seconds_to_time % 3600 // 60
hours = seconds_to_time // 3600 % 24

print(f'Указанное вами время {seconds_to_time} переведено в формат {hours:02}:{minutes:02}:{seconds:02}')
