import logging
import csv
import json
from pathlib import Path
import datetime

"""Задание №1
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль."""


# FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
# logging.basicConfig(level=logging.ERROR, filename='ZeroDivisionError.log', encoding='utf-8',
#                     format=FORMAT, style="{")
# logger = logging.getLogger(__name__)


def func_div_two(a, b) -> float:
    try:
        res = a / b
    except ZeroDivisionError as e:
        logger.error(f'Ошибка деления числа {a} на число {b}')
        return float('inf')
    return res


#
# if __name__ == '__main__':
#     print(func_div_two(8, 0))

"""Задание №2
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging."""

# FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
# logging.basicConfig(level=logging.INFO, filename='deco_file.log',
#                     encoding='utf-8', format=FORMAT, style="{")
# logger = logging.getLogger(__name__)
#
#
# def deco_file(func):
#
#     def wrapper(*args, **kwargs):
#         new_data = {'args': args, **kwargs}
#         result = func(*args, **kwargs)
#         logger.info(new_data)
#         return result
#
#     return wrapper
#
#
# @deco_file
# def call(*args, **kwargs):
#     pass


# call(12, 24, 56, ax=12, b=45)


"""Задание №3
Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат."""

# FORMAT = '{levelname} - {asctime}: {msg}'
# logging.basicConfig(level=logging.INFO, filename='deco_file.log',
#                     encoding='utf-8', format=FORMAT, style="{")
# logger = logging.getLogger(__name__)
#
#
# def deco_file(func):
#
#     def wrapper(*args, **kwargs):
#         new_data = {'args': args, **kwargs}
#         result = func(*args, **kwargs)
#         logger.info(f'{func.__name__} {new_data}')
#         return result
#
#     return wrapper
#
#
# @deco_file
# def call(*args, **kwargs):
#     pass
#
#
# call(12, 24, 56, ax=12, b=45)

"""Задание №4
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату."""

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.error('msg'), filename='deco_file.log',
                    encoding='utf-8', format=FORMAT, style="{")
logger = logging.getLogger(__name__)

from datetime import datetime
from calendar import monthrange

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.ERROR, filename='data_text.log', encoding='utf-8',
                    format=FORMAT, style="{")
logger = logging.getLogger(__name__)

MONTH = ('янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')
DAY = ("пон", "вто", "сре", "чет", "пят", "суб", "вос")


def data_text(text: str) -> datetime:
    try:
        count, day, month = text.split()
    except ValueError as e:
        logger.error(f'Ошибка введения даты')
        return None
    count = int(count[:-2])
    day = DAY.index(day[:3])
    month = MONTH.index(month[:3]) + 1
    year = datetime.now().year
    count_days = monthrange(year, month)[1]
    # print(count_days)
    count_week = 0
    for d in range(1, count_days + 1):
        date = datetime(day=d, month=month, year=year)
        if date.weekday() == day:
            # print(date)
            count_week += 1
            if count == count_week:
                return date

ё
print(data_text('3-я среда мая'))
