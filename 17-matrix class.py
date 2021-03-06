"""Реализуйте класс Matrix. Он должен содержать:
Конструктор от списка списков. Гарантируется, что списки состоят из чисел, не пусты и все имеют одинаковый размер.
Конструктор должен копировать содержимое списка списков, т. е. при изменении списков, от которых была сконструирована
матрица, содержимое матрицы изменяться не должно.
Метод __str__, переводящий матрицу в строку. При этом элементы внутри одной строки должны быть разделены знаками табуляции,
а строки  —  переносами строк. После каждой строки не должно быть символа табуляции и в конце не должно быть переноса строки.
Метод size без аргументов, возвращающий кортеж вида (число строк, число столбцов). Пример теста с участием этого метода
есть в следующей задаче этой недели."""


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


exec(stdin.read())
