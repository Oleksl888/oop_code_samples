'''Создайте функцию, которая создает класс, на основе переданных ей названия, атрибутов и методов.
Необходимо, чтобы все названия переданных атрибутов и методов были приведены к нижнему регистру до
создания класса.'''


def create_class_lower(name, bases, attrs):
    print('Values Before:')
    print(attrs)
    newdict = {}
    for key, val in attrs.items():
        if isinstance(key, str):
            newdict[key.lower()] = val.lower() if isinstance(val, str) else val
    attrs = newdict
    print('Values After:................')
    print(attrs)
    return type(name, bases, attrs)


if __name__ == '__main__':
    class MyClass(metaclass=create_class_lower):
        Name = 'Somename'
        info = 'Someinfo'
        count = 99

        def Get_name(self):
            print(self.Name)

    class AnotherClass(metaclass=create_class_lower):
        Another_name = '1111'
        another_iNfo = 'JJJJJJJ stuff'
        anotHer_count = 101

        def get_Info(self):
            print(self.another_iNfo)

    a = MyClass
    b = AnotherClass
    print(a.__dict__)
    print(b.__dict__)
    print(a.name)
    print(a.Name)