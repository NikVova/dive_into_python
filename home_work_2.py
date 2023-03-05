import fractions
from math import gcd

def choice():
    user_choice = int(input("Выберите функцию:\n 1. Перевод числа из десятичного в шестнадцатеричное.\n 2. Сложение умножение дробей\n Ваш выбор:"))
    if user_choice == 1:
        num_to_hex()
    elif user_choice == 2:
        fraction_user()
    else:
        print("Нет такой функции. До новых встреч!!!")
# № 1
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
def num_to_hex():
    user_num = int(input("Введите целое число:"))
    result = ''
    hex_num = 16
    values = '0123456789ABCDEF'
    print(hex(user_num))
    while user_num > 0 :
        result = values[user_num % 16] + result
        user_num = user_num // 16
    print(result)



# № 2
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
def fraction_user():
    num_1 = input("Введите дроби через пробел в формате a / b c / d:")
    values = []

    def add():
        for item in num_1:
            if item.isnumeric():
                values.append(int(item))

    add()
    def sum_fraction():
        x = values[0] * values[3] + values[1] *values[2]
        y = values[1] * values[3]
        z = gcd(x, y)
        return (x // z, y // z)

    sum_numerator, sum_denumerator = sum_fraction()

    multi_numerator = values[0] * values[2]
    multi_denumerator = values[1] * values[3]
    print(f'{sum_numerator}/{sum_denumerator}, {multi_numerator}/{multi_denumerator}')


    f1 = fractions.Fraction(values[0], values[1])
    f2 = fractions.Fraction(values[2], values[3])
    print(f1 + f2, f1 * f2)

choice()