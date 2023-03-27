import random
import csv
from typing import Callable

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
            for rows in a:
                [a, b, c] = int(rows[0]), int(rows[1]), int(rows[2])
                result = func(a, b, c)
            return result

    return wrapper


def deco_b(func: Callable):
    def wrapper():





@deco_a
def square(k: int, m: int, n: int) -> int:
    disc = abs(m * 2 - 4 * k * n)
    result = (- m + (disc * 0.5)) / (2 * k)
    result2 = (- m - (disc ** 0.5)) / (2 * k)
    # print(result, result2)
    d = [f'"Корень квадратный 1:"{result} , "Корень квадратный 2: "{result2}']
    return d

square()

# def csv_file():
#     sn = []
#     for i in range(random.randint(10,100)):
#         s = []
#         sn.append(s)
#         for i in range(3):
#             l =random.randint(1,999)
#             s.append(str(l))
#         #print(s)
#     #print(sn)
#     with open('3_numbers.csv', 'w', newline='', encoding='utf-8') as file:
#         csv_write = csv.writer(file)
#         for row in sn:
#             csv_write.writerow(row)
# csv_file()


# with open('3_numbers.csv', 'r', newline='', encoding='utf-8') as file:
#     a = csv.reader(file)
#     for row in a:
#         # print(row)
#         *a,b,c = int(row[0]), int(row[1]), int(row[2])
#         [a, b, c] = int(row[0]), int(row[1]), int(row[2])
#         result = square(a, b, c)