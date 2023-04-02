import math

"""№1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь"""


class Circle:

    def __init__(self, radius: float):
        self.radius = radius

    def cirle_len(self):
        return (2 * math.pi * self.radius)

    def area_circle(self):
        return (math.pi * self.radius ** 2)


# my_circle = Circle(10)
# print(my_circle.area_circle(), my_circle.cirle_len())

"""№2
Создайте класс прямоугольник. 
Класс должен принимать длину и ширину при создании экземпляра. 
У класса должно быть два метода, возвращающие периметр и площадь. 
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат."""


class Rectangle:

    def __init__(self, side_a: float, side_b=None):
        self.side_a = side_a
        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def square_rectangle(self):
        return self.side_a * self.side_b

    def len_rectangle(self):
        return (self.side_a + self.side_b) * 2


# rect = Rectangle(5, 10)
# print(rect.len_rectangle(), rect.square_rectangle())

"""№3
Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор. 
У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор. 
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст"""


class Human:

    def __init__(self, name: str, last_name: str, surname: str, age: int):
        self.name = name
        self.last_name = last_name
        self.surname = surname
        self.__age = age

    def birthday_up(self):
        self.__age += 1

    def full_name(self):
        return f'Name{self.name} {self.last_name} {self.surname}'

    def get_age(self):
        return self.__age


# p1 = Human("Ivan", 'Ivanovich', 'Ivanov', 26)
# print(p1.get_age(), p1.full_name(), p1.birthday_up(), p1.get_age())

"""№4
Создайте класс Сотрудник. 
Воспользуйтесь классом человека из прошлого задания. 
У сотрудника должен быть:
шестизначный идентификационный номер
уровень доступа вычисляемый как остаток от деления суммы цифр id на семь"""


class Employee(Human):

    def __init__(self, name: str, last_name: str, surname: str, age: int, ident: str):
        super().__init__(name, last_name, surname, age)
        self.ident = int(ident)
        self.level = None

    def access(self):
        tmp = 0
        for item in str(self.ident):
            tmp += int(item)
        self.level = tmp % 7


# employ = Employee("Ivan", 'Ivanovich', 'Ivanov', 26, 10)
# print(employ.level, employ.access(), employ.level)

"""№5
Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. 
У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
Для каждого класса создайте метод, выводящий информацию специфичную для данного класса."""


class Fauna:
    def __init__(self, name: str, blood_color: str):
        self.name = name
        self.blood_color = blood_color

    def eat(self):
        print(' Need food')


class Birds(Fauna):
    def __init__(self, name: str, blood_color: str, feathers: bool):
        super().__init__(name, blood_color)
        self.feathers = feathers

    def fly(self):
        print('I can fly!')


class Fishes(Fauna):
    def __init__(self, name: str, blood_color: str, gills: bool):
        super().__init__(name, blood_color)
        self.gills = gills


class Reptiles(Fauna):
    def __init__(self, name: str, blood_color: str, scales: bool):
        super().__init__(name, blood_color)
        self.scales = scales


bird = Birds('Кеша', 'красная', True)
print(bird.name)
bird.fly()
bird.eat()
