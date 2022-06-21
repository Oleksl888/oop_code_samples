'''Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий температуру и
позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, причём данные могут
быть заданы в одной шкале, а получены в другой.'''


class Temperature:
    def __init__(self, degrees, scale):
        self.temp = degrees #using setter to set the initial values
        self.scale = scale

    def convert(self):
        if self.scale == 'C':
            self.temp = round((self.temp * 9 / 5) + 32, 2)
            self.scale = 'F'
        elif self.scale == 'F':
            self.temp = round((self.temp - 32) * 5 / 9, 2)
            self.scale = 'C'

    def __str__(self):
        if self.scale == 'C':
            return f'{self.temp} degrees Celcius'
        elif self.scale == 'F':
            return f'{self.temp} degrees Fahrenheit'
        else:
            return 'Incorrect temperature entered'

    @property #This is getter, takes only one parameter - self
    def temp(self):
        return self._degrees

    @temp.setter # This is setter, must take only one parameter. Sets the value
    def temp(self, degrees):
        self._degrees = degrees

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, scale):
        self._scale = scale

temp = Temperature(0, 'C')
print(temp)
temp.convert()
print(temp)
temp.temp = 66
print(temp)
temp.convert()
print(temp)