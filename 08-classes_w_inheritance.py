'''Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех
транспортных средств поля, в наследниках – специфичные для них. Создайте несколько экземпляров.
Выведите информацию о каждом транспортном средстве.'''


class Vehicle:
    def __init__(self, name, color, engine):
        self.name = name
        self.color = color
        self.has_engine = engine

    def __str__(self):
        if self.has_engine:
            return f'{self.name} belongs to class {self.__class__.__name__}. ' \
                   f'It is {self.color} and does have an engine '
        return f'{self.name} belongs to class {self.__class__.__name__}. ' \
               f'It is {self.color} and does not have an engine '


class Car(Vehicle):
    def __init__(self, name, color, engine):
        super().__init__(name, color, engine)
        self.wheels = 4
        self.can_ride = True
        self.gear = 'Auto'
        self.fuel = 'Gasoline'

    def __str__(self):
        return f'{self.name} belongs to class {self.__class__.__name__}. ' \
               f'It is {self.color}, has {self.wheels} wheels, {self.gear} gear and ' \
               f'uses {self.fuel} for fuel.'

    @staticmethod
    def ride():
        print('The car is riding. WROOOOOOM!')


class ElectricCar(Car):
    def __init__(self, name, color, engine):
        super().__init__(name, color, engine)
        self.fuel = 'Electricity'

    @staticmethod
    def ride():
        print('Riding without emmissions. WEEEEEEE')


class Plane(Vehicle):
    def __init__(self, name, color, engine):
        super().__init__(name, color, engine)
        self.wheels = 'Plenty'
        self.can_ride = True
        self.can_fly = True
        self.fuel = 'Kerosine'

    def __str__(self):
        return f'{self.name} belongs to class {self.__class__.__name__}. ' \
               f'It is {self.color}, has {self.wheels} wheels, and ' \
               f'uses {self.fuel} for fuel. Plane can both ride and fly.'

    @staticmethod
    def ride():
        print('The plane is riding. WROOOOOOM!')

    @staticmethod
    def fly():
        print('The plane is flying. WEEEEEEEEE')


class Boat(Vehicle):
    def __init__(self, name, color, engine):
        super().__init__(name, color, engine)
        self.can_sail = True
        self.fuel = 'Diesel'

    def __str__(self):
        a = super().__str__()
        b = 'The boat can move on water'
        return a + ' ' + b

    @staticmethod
    def sail():
        print('Boats and Hoes!!')


if __name__ == '__main__':
    obj1 = Vehicle('Bike', 'Blue', False)
    print(obj1)
    obj2 = Vehicle('Car', 'green', True)
    print(obj2)
    obj1 = Car('Volks', 'Blue', 1)
    print(obj1)
    obj1.ride()
    obj = Plane('Boeing', 'white', True)
    print(obj)
    obj.ride()
    obj.fly()
    obj2 = ElectricCar('Tesla', 'black', 1)
    print(obj2)
    obj2.ride()
    obj1 = Boat('Zodiac', 'white', 1)
    print(obj1)
    obj1.sail()