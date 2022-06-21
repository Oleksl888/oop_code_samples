"""Добавьте в предыдущий класс следующие методы:
 __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
 __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
 __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент находится справа.
 Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul__."""


from sys import stdin
from copy import deepcopy


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
        newmatrix = []
        for i in range(len(self.mylist)):
            newlist = []
            for j in range(len(self.mylist[0])):
                newlist.append(self.mylist[i][j] + other.mylist[i][j])
            newmatrix.append(newlist)
        return Matrix(newmatrix)

    def __mul__(self, number):
        newmatrix = []
        for i in range(len(self.mylist)):
            newlist = []
            for j in range(len(self.mylist)):
                newlist.append(self.mylist[i][j] * number)
            newmatrix.append(newlist)
        return Matrix(newmatrix)

    __rmul__ = __mul__


exec(stdin.read())
