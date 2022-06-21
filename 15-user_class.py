'''Задание
Создайте класс пользователя (ФИО, дата рождения), к каждому методу составьте doctrings и
постарайтесь максимально следовать правилам, описанным в PEP 8. Вы можете создавать любое количество методов,
с целью потренироваться, но как минимум класс должен содержать:
1. get_short_name
2. get_full_name
3. get_age
4. get_initials
5. set_full_name (принимаем строку вида «Петров Иван Иванович», которую необходимо разбить по
соответствующим полям. Условимся, что порядок будет следующим: Фамилия Имя Отчество)
Создайте код, который будет использовать все разработанные вами методы и поля, соблюдая PEP 8.'''


class User:
    """Class that has some methods.
    __init__ method does not have last name - that attribute is set in the property setter"""

    def __init__(self, mid):
        self.__fname = ''
        self.middle_name = mid
        self.age = ''

    @property
    def name(self):
        return self.__fname

    @name.setter
    def name(self, value):
        self.__fname = value

    @property
    def last_name(self):
        """Returns last name"""
        return self.__lname

    @last_name.setter
    def last_name(self, value):
        """Sets last name"""
        self.__lname = value

    def set_age(self):
        """Takes user input in a loop and sets age value"""
        while True:
            try:
                _age = int(input('Enter your age: '))
            except (TypeError, ValueError):
                print('Age must be only digits. Try again')
            else:
                self.age = _age
                break

    def get_short_name(self):
        """Returns short version of name. If initials not set, returns and error message"""
        try:
            shorty = f'{self.__lname.capitalize()} {self.__fname[0].upper()}. {self.middle_name[0].upper()}.'
        except (IndexError, AttributeError):
            print('First name or middle name is not set')
        else:
            return shorty

    def get_full_name(self):
        """Returns full version of name. If initials not set, returns and error message"""
        try:
            full = f'{self.__lname.capitalize()} {self.__fname.capitalize()} {self.middle_name.capitalize()}'
        except (IndexError, AttributeError):
            print('First name or middle name is not set')
        else:
            return full

    def get_age(self):
        """Returns age. If it is not set, returns and error message"""
        try:
            _age = self.age
        except AttributeError:
            print('Age is not set')
        else:
            return _age

    def get_initials(self):
        """Returns initials. If initials not set, returns and error message"""
        try:
            initials = f'{self.__fname[0].upper()} {self.middle_name[0].upper()}'
        except (IndexError, AttributeError):
            print('First name or middle name is not set')
        else:
            return initials

    def set_full_name(self, name, mid, last):
        """Setter for all three fields. Uses properties to access private fields such as __lname and __fname"""
        self.name = name
        self.middle_name = mid
        self.last_name = last

    def __str__(self):
        return f"This is an instance of {self.__class__.__name__} with fields " \
               f"{self.name}, {self.last_name}, {self.middle_name}"


if __name__ == '__main__':
    alex = User('Serg')
    print(alex.get_short_name())
    alex.name = 'Alex'
    print(alex.get_short_name())
    alex.last_name = 'Slius'
    print(alex.get_short_name())
    alex.set_age()
    print(alex.age)
    print(alex.get_full_name())
    print(alex.get_age())
    print(alex.get_initials())
    alex.set_full_name("A", "B", "C")
    print(alex)