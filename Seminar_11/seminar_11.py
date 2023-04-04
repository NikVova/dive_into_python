import datetime
import time

"""№1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)"""


class MyString(str):
    """Class str"""

    def __new__(cls, value: str, author: str):
        """create new instance"""
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance
    def __init__(self, value, author):
        """Инициализация"""
        self.value = value
        self.author = author

    def __str__(self):
        """Отображение для пользователя"""
        return f'Класс записывает строку {self.value}, автора {self.author} и время{time.time()}'

    def __repr__(self):
        """Отображение для разработчика"""
        return f'(String {self.value}, {self.author}, {time.time()})'


if __name__ == '__main__':
    s = MyString("jdfosdfiosdfis", "Tryry")
    print(s)
    print(repr(s))
#     print(s.time)
#     print(s.author)

"""№2
Создайте класс Архив, который хранит пару свойств. Например, число и строку. 
При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
list-архивы также являются свойствами экземпляра"""


class Archive:
    """Save old value"""
    _instance = None

    def __init__(self, num: int, val: str):
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.number = []
            cls._instance.value = []
        else:
            cls._instance.number.append(cls._instance.num)
            cls._instance.value.append(cls._instance.val)
        return cls._instance


# if __name__ == '__main__':
#     s = Archive(123, 'sdf')
#     print(s.number, s.value)
#
#     s = Archive(5887, 'Hello')
#     print(s.number, s.value)
#     s = Archive(8952, 'Hi')
#     print(s.number, s.value)

"""№3
Добавьте к задачам 1 и 2 строки документации для классов"""

# help(MyString)

"""№4
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя."""


class Archive:
    """Save old value"""
    _instance = None

    def __init__(self, num: int, val: str):
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.number = []
            cls._instance.value = []
        else:
            cls._instance.number.append(cls._instance.num)
            cls._instance.value.append(cls._instance.val)
        return cls._instance

    def __str__(self):
        return f'Класс записывает число {self.num} и строку {self.val} в словарь'

    def __repr__(self):
        return f'(Archive {self.number}, {self.value})'


# if __name__ == '__main__':
#     s = Archive(123, 'sdf')
#     print(s.number, s.value)
#
#     s = Archive(1234, 'sasdf')
#     print(s.number, s.value)
#     print({s})
#     print(s)

"""№5
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений."""


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

    def __add__(self, other):
        a = self.side_a + other.side_a
        b = self.side_b + other.side_b
        return Rectangle(a, b)

    def __sub__(self, other):
        if self.len_rectangle() < other.len_rectangle():
            self, other = other, self
        a = self.side_a - other.side_a
        b = self.side_b - other.side_b
        return Rectangle(a, b)


if __name__ == '__main__':
    rect = Rectangle(5, 10)
    # print(rect.len_rectangle(), rect.square_rectangle())
    rect_1 = Rectangle(4, 8)
    rect_2 = rect + rect_1
    print(rect.len_rectangle(), rect_1.len_rectangle(), rect_2.len_rectangle())
    rect_3 = rect - rect_1
    print(rect.len_rectangle(), rect_1.len_rectangle(), rect_2.len_rectangle(), rect_3.len_rectangle())
    print(f'first side {rect_2.side_a}, second side {rect_2.side_b}')
