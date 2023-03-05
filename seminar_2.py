import sys
import math
import decimal


# №1
# a = 7
# b = 7.5
# txt = "message"
# c = {1, 2, 3}
# d = True
#
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(txt))
# print(type(d))

# №2
# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# *Добавьте в список повторяющиеся элементы и сравните на результаты.
# data = ["text", 4, 4.6, True, 455, "hash"]
# for i, num in enumerate(data, start=1):
#     print(i, num, id(num), sys.getsizeof(num), hash(num), end=" ")
#     if isinstance(num, int):
#         print("Целое число" ,num)
#     elif isinstance(num, str):
#         print("Строка", num)

# № 3
# Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата, а не для решения.

# number: int = int(input("Enter number:"))
# number1: int = number
# res = ""
# double = 2
# octy = 8
# print(bin(number))
# print(oct(number))
# for i in double, octy:
#     number: int = number1
#     res: str = ""
#     while number > 0:
#         double_num: int = number % i
#         res = str(double_num) + res
#         number = number // i
#     print(res)

# № 4
# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять не менее 42 знаков после запятой.
#
# decimal.getcontext().prec = 42
# diametr: decimal.Decimal = decimal.Decimal(input("Введите диаметр:"))
# pi = decimal.Decimal(math.pi)
# max_limit = 1000
# if diametr <= max_limit:
#     lenght_krug = pi * diametr
#     square = pi * (diametr / 2) ** 2
#     print(lenght_krug, square)
# else:
#     print("Введено слишком большое значение")

# № 5
# Напишите программу, которая решает квадратные уравнения
# даже если дискриминант отрицательный.

a = int(input("Введите первое значение:"))
b = int(input("Введите второе значение:"))
c = int(input("Введите третье значение:"))

disc = abs(b ** 2 - 4 * a * c)
x1 = (- b + disc ** 0.5) / (2 * a)
x2 = (- b - disc ** 0.5) / (2 * a)

print(x1, x2)