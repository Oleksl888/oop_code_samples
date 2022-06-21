"""Перепишите решение первого задания с помощью генератора."""


class BackwardsIter:
    def __init__(self, somelist):
        self.somelist = somelist
        self.length = len(somelist)

    def __iter__(self):
        index = self.length - 1
        while index >= 0:
            yield self.somelist[index]
            index -= 1


mylist = [1, 2, 3, 4, 5]
it = BackwardsIter(mylist)
for i in it:
    print(i)

