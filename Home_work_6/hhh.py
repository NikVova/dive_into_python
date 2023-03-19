""" Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками. Функция в цикле вызывает
 загадывающую функцию, чтобы передать ей все свои загадки.
 """

from DZsixth1a import *

all = ['mystery']


def mystery(chanse: int) -> str:
    USER = myst_list(int(input("Enter number from 0 to 2 ")))
    for i in range(chanse):

        print(USER[0])
        ans = input('Enter aswer:  ')
        if ans == USER[1]:
            return 'You guess!!!'
        else:
            chanse + 1

    return 0


if name == 'main':
    print(mystery(2))

all = ['myst_list']


def myst_list(a: int):
    ml = {
        'На верхушке стебелька солнышко и облака': 'ромашка',
        'Серые комочки на красненьком пруточке': 'верба',
        'Зимой и летом одним цветом! ': 'Елка',
    }
    m = (list(ml.items())[a])
    return m


if name == 'main':
    print(myst_list(int(input("Enter number from 0 to 2 "))))

""" Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
Проверку года на високосность вынести в отдельную защищённую функцию.
"""

from datetime import date

all = ['date_check', 'leap']

def date_check(d:int, m: int, y: int) -> bool:
    try:
        date(y, m, d)
        return True
    except:
        return False

def leap(y: int) -> bool:
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False


if name == 'main':
    e = input('Enter date as DD.MM.YYYY: ')
    a, b, c = e.split('.')
    d = int(a)
    m = int(b)
    y = int(c)
    print(date_check(d, m, y), leap(y))