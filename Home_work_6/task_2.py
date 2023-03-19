""" Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""

from datetime import date

__all__ = ['date_check', 'leap', 'user_num']


def date_check(d: int, m: int, y: int) -> bool:
    try:
        date(y, m, d)
        return True
    except:
        return False


def leap(d: int, m: int, y: int) -> bool:
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return "Високосный"
    else:
        return "Не високосный"


def user_num(user_str: str) -> int:
    user_str = input('Введите дату в формате DD.MM.YYYY: ')
    a, b, c = user_str.split('.')
    d = int(a)
    m = int(b)
    y = int(c)
    return d, m, y


if __name__ == 'main':
    print(date_check(*(user_num(user_str='11.11.1111'))))
    print(leap(*(user_num(user_str='11.11.1111'))))