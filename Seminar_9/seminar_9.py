from typing import Callable
import random
import json
from pathlib import Path
import time

# __all__ = ['game', 'ugadai', 'call']

"""№1
Создайте функцию-замыкание, которая запрашивает два целых числа:
от 1 до 100 для загадывания,
от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток."""

# def deco(a: int, count: int) -> Callable[[], None]:
#
#     def ugadai() -> None:
#         for i in range(count):
#             num = int(input('Enter 1-100: '))
#             if num > a:
#                 print("Число больше! ")
#             elif num < a:
#                 print("Число меньше! ")
#             else:
#                 print("You win!")
#                 break
#     return ugadai
#
# game = deco(20, 5)

# game()

"""№2
Дорабатываем задачу 1. 
Превратите внешнюю функцию в декоратор. 
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10]. 
Если не входят, вызывать функцию со случайными числами из диапазонов.
"""


def deco(func):
    def wrapper(a: int, count: int):
        if a < 1 or a > 100:
            a = random.randint(1, 101)
        if count < 1 or count > 10:
            count = random.randint(1, 11)
        result = func(a, count)
        return result
    return wrapper


@deco
def ugadai(a: int, count: int) -> None:
    for i in range(count):
        num = int(input('Enter 1-100: '))
        if num > a:
            print("Число больше! ")
        elif num < a:
            print("Число меньше! ")
        else:
            print("You win!")
            break


# ugadai(300, 300)

"""№3
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.
"""

def deco_file(func):
    file = Path(f'{func.__name__}.json')
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []
    def wrapper(*args, **kwargs):
        new_data = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        data.append(new_data)
        with open(file, 'w', encoding='utf-8') as f1:
            json.dump(data, f1)
        return result
    return wrapper

@deco_file
def call(*args, **kwargs):
    pass


# call(12, 24, 56, ax = 12, b = 45)

"""№4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой функции."""

def count(num: int = 1):
    def deco(func: Callable):
        # @wraps(func)
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f'Результаты замеров {time_for_count}')
            return result
        return wrapper
    return deco

@count(10)
def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print(f'{factorial(10) = }')
print(f'{factorial(10) = }')