import re

"""Задание №1
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""

# def clean_text(text: str) -> str:
#
#     cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
#     return cleaned_text.lower()


# user_text = "Every утро i go на work! 12334_12"
# print(clean_text("hello world"))


# from string import ascii_letters
#
# def delfromtext(text: str):
#     a = ''
#     for char in text:
#         if char in ascii_letters or char == ' ':
#             a += char
#     return a.lower()


# print(delfromtext('роме букв латинского. алфавита 123/ апраоп! hjjkg'))

"""Задание №2
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)"""

def clean_text(text: str) -> str:
    """
    >>> clean_text("hello world")
    'hello world'
    >>> clean_text("HeLLo World")
    'hello world'
    >>> clean_text("HeLLo! World!")
    'hello world'
    >>> clean_text("HeLLo World во")
    'hello world '
    >>> clean_text("HeLLo World вол_шебСт0_12")
    'hello world '
    """
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower()


# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod(verbose=True)

"""Задание №3
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)"""

import unittest

def clean_text(text: str) -> str:
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower()


class TestCaseName(unittest.TestCase):

    def test_no_change(self):
        self.assertEqual(clean_text("hello world"), 'hello world')

    def test_registr(self):
        self.assertEqual(clean_text("Hello World"), 'hello world')

    def test_no_punctuation(self):
        self.assertEqual(clean_text("Hello, World."), 'hello world')

    def test_language(self):
        self.assertEqual(clean_text("Hello World. Привет"), 'hello world ')

    def test_all(self):
        self.assertEqual(clean_text("Hello World.! Привет"), 'hello world ')
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)


"""Задание №4
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)"""

import pytest

def clean_text(text: str) -> str:
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower()


def test_no_change():
    assert clean_text("hello world") == 'hello world', 'no_change'


def test_registr():
    assert clean_text("Hello World") == 'hello world', 'registr'


def test_no_punctuation():
    assert clean_text("Hello, World.") == 'hello world', 'punctuation'


def test_language():
    assert clean_text("Hello World. Привет") == 'hello world ', 'language'


def test_all():
    assert clean_text("Hello World.! Привет") == 'hello world ', 'all'

#
# if __name__ == '__main__':
#     pytest.main(['-vv'])

"""Задание №5
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса."""


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


class TestCaseName(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(5, 15)
        self.r2 = Rectangle(5, 5)
        self.r3 = Rectangle(5, 10)

    def test_sqare(self):
        self.assertEqual(self.r1.square_rectangle(), 75)

    def test_len(self):
        self.assertEqual(self.r1.len_rectangle(), 40)


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
