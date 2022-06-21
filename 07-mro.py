'''Создайте иерархию классов с использованием множественного наследования. Выведите на экран
порядок разрешения методов для каждого из классов. Объясните, почему линеаризации данных
классов выглядят именно так.'''


class A:
    def method(self):
        print('This is class A')


class B(A):
    def another_method(self):
        print('This is class B')


class C(A):
    def method(self):
        print('This is method C')


class D(C, B):
    pass


class E(B, C):
    pass


#class F(D, E):
    #pass

for name in [A,B,C,D,E]:
    print(name.mro())

d = D()
e = E()
d.method()
d.another_method()
e.method()
e.another_method()