import math
import doctest
import unittest
import pytest


def cirle_len(radius):  # doctest
    """
    >>> cirle_len(10)
    62.83185307179586
    >>> cirle_len(-10)
    -62.83185307179586
    >>> cirle_len(0)
    0.0
    >>> cirle_len(d)
    Traceback (most recent call last):
      File "D:\Разраб\ПВП\dive_into_python\Home_work_14\home_work_14.py", line 25, in <module>
        print(cirle_len(d))
    NameError: name 'd' is not defined
    >>> cirle_len()
    Traceback (most recent call last):
        File "D:\Разраб\ПВП\dive_into_python\Home_work_14\home_work_14.py", line 28, in <module>
            print(cirle_len())
    TypeError: cirle_len() missing 1 required positional argument: 'radius'
    """
    return 2 * math.pi * radius


def area_circle(radius):
    return math.pi * radius ** 2


# class TestCaseName(unittest.TestCase):
#
#     def test_positive(self):
#         self.assertEqual(area_circle(5), 78.53981633974483)
#
#     def test_negative_radius(self):
#         self.assertEqual(area_circle(-5), 78.53981633974483)
#
#     def test_zero(self):
#         self.assertEqual(area_circle(0), 0.0)
#
#     def test_big_radius(self):
#         self.assertEqual(area_circle(1_000_000_000), 3.1415926535897933e+18)
#

def duplicate_num(*args) -> list[int]:
    """Создает новый список дубликатов без повторений"""
    list_1 = [*args]
    print(list_1)
    list_2 = []
    for item in list_1:
        if list_1.count(item) > 1 and item not in list_2:
            for i in range(list_1.count(item)):
                if item not in list_2:
                    list_2.append(item)
    return list_2


def test_positive():
    assert duplicate_num(1, 2, 3, 2, 5, 1, 6, 2, 4, 1, 5, 8, 7, 9, 7, 0) == [1, 2, 5, 7]


def test_no_args():
    assert duplicate_num() == []


def test_negative_args():
    assert duplicate_num(-1, -2, -2, -3, -2, -2) == [-2]


def test_letters():
    assert duplicate_num('b', 'd', 'b') == ['b']

def test_all():
    assert duplicate_num('b', 'd', 'b', 1, 1, 2, 3, 'Ы', 'и', 'Ы') == ['b', 1, 'Ы']

if __name__ == '__main__':
    doctest.testmod(verbose=True)
    # unittest.main(verbosity=2)
    # pytest.main([-vv])
