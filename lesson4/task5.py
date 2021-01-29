from functools import reduce

my_list = list(range(100, 1001))
my_list = [el for el in my_list if el % 2 == 0]
result = reduce(lambda x, y: x * y, my_list)

print(f'Результат: {result}')
