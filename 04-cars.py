'''Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.'''

class Car():
    def __init__(self, name, color, gear, type_gas='benzine'):
        self.name = name
        self.color = color
        self.gear = gear
        self.type_gas = type_gas
        self.price = None

    @staticmethod
    def beep():
        print('WROOOOOOM')

    def set_price(self, value):
        self.price = value

    def get_price(self):
        return self.price


class Dealership():
    def __init__(self, cars_list):
        self.cars_list = cars_list
        self.money = 10000

    def get_car_list(self):
        for car in self.cars_list:
            print(f'''
Name:{car.name} 
Color:{car.color} 
Gear:{car.gear} 
Type of Fuel:{car.type_gas} 
Price: ${car.price}''')
            print('----------------------')

    def set_price(self, car, val):
        for name in self.cars_list:
            if name.name == car:
                name.price = val
                print(f'''
The new price has been set
    Name:{name.name} 
    Color:{name.color} 
    Gear:{name.gear} 
    Type of Fuel:{name.type_gas} 
    Price: ${name.price}''')
    print('----------------------')

    def sell_car(self, car):
        for num, name in enumerate(self.cars_list):
            if name.name == car:
                self.money += name.price
                print(f'{name.name} has been sold for {name.price}')
                print('Available for sale:')
                del self.cars_list[num]
                return self.get_car_list()
        print("Car is not available for sale")


if __name__ == '__main__':
    car1 = Car('Volkswagen', 'Blue', 'auto')
    car2 = Car("Lanos", 'silver', 'manual')
    car3 = Car("Lambo", 'yellow', 'auto', 'diesel')
    cars = [car1, car2, car3]
    myshop = Dealership(cars)
    myshop.set_price('Lanos', 10000)
    myshop.set_price('Lambo', 100000)
    myshop.set_price('Volkswagen', 20000)
    myshop.sell_car('Volkswagen')
    myshop.sell_car('Lanos')
    print(myshop.money)