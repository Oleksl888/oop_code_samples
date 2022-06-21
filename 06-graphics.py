'''Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать
нажатия мыши. Опишите класс кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите
метод нажатия на кнопку.'''
import random


class GraphObject:
    def __init__(self):
        self.x = 0
        self.y = 0

    def render(self):
        print(f'I am a {self.__class__.__name__}')
        self.draw()

    def draw(self):
        print(f'These are my coordinates: x:{self.x}, y:{self.y}')


class ResponsiveObject(GraphObject):
    def onclick(self):
        print('Click!\nReading coordinates')
        self.x = random.randint(-1000, 1000)
        self.y = random.randint(-1000, 1000)


class Rectangle(GraphObject):
    def __init__(self, side1, side2):
        super().__init__()
        self.a = side1
        self.b = side2

    def draw(self):
        for i in range(self.a):
            for j in range(self.b):
                print('#', end=' ')
            print()

class Button(ResponsiveObject, Rectangle):
    def onclick(self):
        print('Click Inside the rectangle!\nReading coordinates')
        self.x = random.randint(0, self.a)
        self.y = random.randint(0, self.b)

    def draw(self):
        super(GraphObject, self).draw()


if __name__ == '__main__':
    obj1 = GraphObject()
    obj1.render()
    obj2 = Rectangle(5, 4)
    obj2.render()
    obj3 = ResponsiveObject()
    obj3.render()
    obj3.onclick()
    obj3.render()
    obj4 = Button(5, 5)
    obj4.render()
    obj4.onclick()
    obj4.render()