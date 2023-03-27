import random
import csv
from typing import Callable
import json
__all__ = ['deco_a', 'deco_b', 'random', 'square']

""" 1.Написать функции:
-Нахождение корней квадратного уравнения
-Генерации csv файла с 3 случайными числами в каждой строке 100-1000 строк
-Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждойй тройкой чисел из csv файла
-Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
2. Соберите пакет из файлов
"""


def deco_a(func: Callable):
    def wrapper():
        with open('3_numbers.csv', 'r', newline='', encoding='utf-8') as file:
            a = csv.reader(file)
            result = []
            for rows in a:
                [a, b, c] = int(rows[0]), int(rows[1]), int(rows[2])
                result.append(func(a, b, c))
            return result

    return wrapper


def deco_b(func: Callable):
    def wrapper():
        result = func()
        print(result, 'deco_b')
        with open('3_numbers.json', 'w') as f:
            json.dump(result, f, indent=2)

    return wrapper

@deco_b
@deco_a
def square(k: int, m: int, n: int) -> int:
    disc = abs(m * 2 - 4 * k * n)
    result = (- m + (disc * 0.5)) / (2 * k)
    result2 = (- m - (disc ** 0.5)) / (2 * k)
    d = [f'{result}, {result2}]']
    return d


square()


def csv_file():
    sn = []
    for i in range(random.randint(10, 100)):
        s = []
        sn.append(s)
        for _ in range(3):
            l: int = random.randint(1, 999)
            s.append(str(l))
    with open('3_numbers.csv', 'w', newline='', encoding='utf-8') as file:
        csv_write = csv.writer(file)
        for row in sn:
            csv_write.writerow(row)


csv_file()


