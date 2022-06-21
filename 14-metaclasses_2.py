'''Создайте метакласс, записывающий в файл всю информацию о классах, которые используют его в качестве метакласса.'''


class Meta(type):
    # def __init__(cls, name, bases, attrs):
    #     super().__init__(name, bases, attrs)
    #     cls.common_attr = 888
    #     with open('info.txt', 'a') as file:
    #         file.write(cls.__name__)
    #         file.write('\n')
    #         file.write(str(cls.__bases__))
    #         file.write('\n')
    #         file.write(str(cls.__mro__))
    #         file.write('\n')
    #         file.write(str(cls.__dict__))
    #         file.write('\n')
    def __new__(cls, name, base, attrs):
        cls.common_attr = 8888
        with open('info.txt', 'a') as file:
            print(name, file=file)
            print(base, file=file)
            print(attrs, file=file)
            print(cls.__dict__, file=file)
        return type.__new__(cls, name, base, attrs)


if __name__ == '__main__':
    class MyClass(metaclass=Meta):
        name = 'Somename'
        info = 'Someinfo'
        count = 99

        def get_name(self):
            print(self.name)

    class AnotherClass(metaclass=Meta):
        another_name = '1111'
        another_info = 'more stuff'
        another_count = 101

        def get_info(self):
            print(self.another_info)

    a = MyClass
    b = AnotherClass
    print(a.common_attr)
    print(b.common_attr)
    b.common_attr = 22
    print(a.common_attr)
    print(b.common_attr)