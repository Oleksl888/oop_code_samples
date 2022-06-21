"""Добавьте в программу из предыдущей задачи класс MatrixError, содержащий внутри self поля matrix1 и matrix2 — ссылки на матрицы.
В класс Matrix внесите следующие изменения:
Добавьте в метод __add__ проверку на ошибки в размере входных данных, чтобы при попытке сложить матрицы разных размеров
было выброшено исключение MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым аргументом __add__
(просто self), а matrix2  —  вторым (второй операнд для сложения).
Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует экземпляр класса Matrix)
Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу. Пример статического метода."""


from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, mat1, mat2):
        self.matrix1 = mat1
        self.matrix2 = mat2


class Matrix:
    def __init__(self, mylist):
        self.mylist = deepcopy(mylist)

    def __str__(self):
        line = ''
        for lst in self.mylist:
            for i in range(len(lst)):
                if i != len(lst) - 1:
                    line += str(lst[i]) + '\t'
                else:
                    if lst is not self.mylist[-1]:
                        line += str(lst[i]) + '\n'
                    else:
                        line += str(lst[i])
        return line

    def size(self):
        return len(self.mylist), len(self.mylist[0])

    def __add__(self, other):
        if len(self.mylist) == len(other.mylist):
            newmatrix = []
            for i in range(len(self.mylist)):
                newlist = []
                for j in range(len(self.mylist[0])):
                    newlist.append(self.mylist[i][j] + other.mylist[i][j])
                newmatrix.append(newlist)
            return Matrix(newmatrix)
        else:
            error = MatrixError(Matrix(self.mylist), Matrix(other.mylist))
            raise error

    def __mul__(self, number):
        newmatrix = []
        for i in range(len(self.mylist)):
            newlist = []
            for j in range(len(self.mylist)):
                newlist.append(self.mylist[i][j] * number)
            newmatrix.append(newlist)
        return Matrix(newmatrix)

    __rmul__ = __mul__

    def transpose(self):
        newmatrix = []
        for i in range(len(self.mylist[0])):
            new = []
            for j in range(len(self.mylist)):
                new.append(self.mylist[j][i])
            newmatrix.append(new)
        self.mylist = newmatrix
        return Matrix(newmatrix)

    @staticmethod
    def transposed(matrix):
        newmatrix = []
        for i in range(len(matrix.mylist[0])):
            new = []
            for j in range(len(matrix.mylist)):
                new.append(matrix.mylist[j][i])
            newmatrix.append(new)
        return Matrix(newmatrix)


exec(stdin.read())
