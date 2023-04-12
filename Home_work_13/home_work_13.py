""" Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра. У класса должно быть два метода, возвращающие
длину окружности и её площадь
"""
import math


class Round:
    def __init__(self, radius: float) -> None:
        if type(radius) == float:
            self.radius = radius
        else:
            raise ValueError(f'Enter a real mumber')

    def length(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius ** 2


round = Round(10)
print(round.length(), round.square())

""" Создайте класс прямоугольник. 
Класс должен принимать длину и ширину при создании экземпляра. У класса должно быть два метода, возвращающие периметр и площадь. 
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат."""


class Rectangle:

    def __init__(self, side_a: float, side_b=None):
        if side_a <= 0:
            raise ValueError(f'value must be greater than 0')
        else:
            self.side_a = side_a
            if side_b is None:
                self.side_b = side_a
            elif side_b <= 0:
                raise ValueError(f'value must be greater than 0')
            else:
                self.side_b = side_b

    def square_rectangle(self):
        return self.side_a * self.side_b

    def len_rectangle(self):
        return (self.side_a + self.side_b) * 2


rect = Rectangle(5, -10)
print(rect.len_rectangle(), rect.square_rectangle())
