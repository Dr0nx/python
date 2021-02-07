"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""

from random import randint


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join([f'{col}'
                                    for col in row])
                          for row in self.matrix])

    def __add__(self, other):
        res = Matrix(self)
        res.matrix = []
        for j in range(len(self.matrix)):
            temp = []
            for k in range(len(self.matrix[j])):
                x = self.matrix[j][k] + other.matrix[j][k]
                temp.append(x)
            res.matrix.append(temp)
        return res


x, y = 3, 4
m1 = [[randint(1, 99) for col in range(y)] for row in range(x)]
m2 = [[randint(1, 99) for col1 in range(y)] for row1 in range(x)]
matrix1 = Matrix(m1)
matrix2 = Matrix(m2)
print(f'Матрицы сгенерированы размером {x} на {y} и заполнены случайными числами.\n')
print(f'Матрица 1:\n{matrix1}\n\nМатрица 2:\n{matrix2}\n')
print(f'Результат суммы чисел matrix1 + matrix2:\n{matrix1 + matrix2}')
