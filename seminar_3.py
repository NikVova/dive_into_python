# № 1
# Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные
# (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
#
# list_1 = [1, 2, 3, 5, 6, 2, 6, 1, 3, 5]
# list_2 = [ ]
# for item in list_1:
#     if item not in list_2:
#         list_2.append(item)
#
# print(list_2)
#
# list_3 = list(set(list_1))
#
# print(list_3)

# №2
# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях

# user_string = input("Введите данные:")
# result  = ''
# if user_string.isdecimal():
#     result = int(user_string)
# elif user_string.replace('.', '').replace('-','').isdecimal():
#     result = float(user_string)
# elif not user_string.islower():
#     result = user_string.lower()
# else:
#     result = user_string.upper()
#
#
# print(f'{result}', {type(result)})

# №3
# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где
# ключ - тип элемента,
# значение - список элементов данного типа.

# my_typle = (1, 5.6, "text", True, False, 0, 6, 3.4)
#
# my_dict = {}
# for item in my_typle:
#     # if type(item) in my_dict.keys():
#     #     my_dict[type(item)] = item
#
#     key = my_dict.setdefault(type(item),list())
#     key.append(item)
#
# print(my_dict)

#№4
# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

# list_1 = [1, 2 , 3, 2, 5, 1, 6, 2, 4, 1, 5, 8, 7, 9, 0]
# for item in list_1:
#     if list_1.count(item) > 1:
#         for i in range(list_1.count(item)):
#             list_1.remove(item)
#
# print(list_1)

# №5
# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.
#
# list_1 = [1, 2, 3, 2, 5, 1, 6, 2, 4, 1, 5, 8, 7, 9, 0]
# list_2 = []
#
# for i, item in enumerate(list_1, start=1):
#     if item % 2 != 0:
#         list_2.append(i)
#
# print(list_2)

# № 6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки

user_string = input("Введите строку:").split()
user_string.sort()
max_len_temp = 0
for item in user_string:
    if len(item) > max_len_temp:
        max_len_temp = len(item)
for i, k in enumerate(user_string, start=1):
    print(f'{i} {k:<{max_len_temp}}')
