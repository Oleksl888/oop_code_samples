"""Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог
reversed)."""


class BackwardsIter:
    def __init__(self, somelist):
        self.somelist = somelist
        self.length = len(somelist)

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        index = self.length - 1
        if index < 0:
            raise StopIteration
        else:
            self.length -= 1
            return self.somelist[index]


mylist = [1, 2, 3, 4, 5]
it = BackwardsIter(mylist)
for i in it:
    print(i)

