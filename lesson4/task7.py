def fact(n):
    fa = 1
    for num in range(2, n + 1):
        fa *= num
        yield fa


try:
    number = int(input('Введите конечное число n: '))
except ValueError:
    print('Небходимо целое положительное число')
else:
    for el in fact(number):
        print(el)

