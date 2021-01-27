def my_func1(x, y):
    return x ** y


def my_func2(x, y):
    result = 1
    count = 0

    while count > y:
        result /= x
        count -= 1

    return result


try:
    raised = float(input("Введите действительное положительное число x: "))
    power = int(input("Введите целое отрицательное число y: "))
    if power >= 0:
        print("Необходимо ввести целое отрицательное число!")

    print("Первый метод: возведение в степень с помощью оператора **: ", my_func1(raised, power))
    print("Второй метод: использование цикла: ", my_func2(raised, power))
except ValueError:
    print("Необходимо ввести число!")
