'''Создайте метакласс, который проверяет класс на запрет использования цифр в именах атрибутов и методах,

а также верхнего регистра. Генерировать исключение, если данные правила нарушены.'''


class MyException(Exception):
    def __init__(self, *args):
        print('Unaccepted characters in ', end=' ')
        for name in args:
            print(name, end=' ')


class Meta(type):
    def __new__(cls, name, bases, attrs):
        for key in attrs.keys():
            if isinstance(key, int) or isinstance(key, float):
                raise MyException(key)
            elif not key.islower():
                raise MyException(key)
            elif isinstance(key, str):
                for char in key:
                    if char.isdigit():
                        raise MyException(key)
        return type.__new__(cls, name, bases, attrs)


if __name__ == '__main__':
    class MyClass(metaclass=Meta):
        name = 'omename'
        info = 'Someinfo'
        count = 99

        def get_name(self):
            print(self.name)

    class AnotherClass(metaclass=Meta):
        another_name = '1111'
        another_info = 'JJJJJJJ stuff'
        another_count = 101

        def get_info(self):
            print(self.another_iNfo)

    a = MyClass
    b = AnotherClass
    print(a.__dict__)
    print(b.__dict__)
    print(a.name)
