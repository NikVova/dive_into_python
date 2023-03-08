"""№1
Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы
Слова выводятся отсортированными согласно кодировки Unicode
Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки"""

def str_sort():
    user_string = input("Введите строку:").split()
    user_string.sort()
    max_len_temp = 0
    for item in user_string:
        if len(item) > max_len_temp:
            max_len_temp = len(item)
    for i, k in enumerate(user_string, start=1):
        print(f'{i} {k:<{max_len_temp}}')

# str_sort()


""""№2
Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию."""


def str_unicode(text: str) -> list[int]:
    result = set()

    for char in text:
        result.add(ord(char))
    result = sorted(result, reverse=True)
    return result

# print(str_unicode(input("Введите текст:")))



"""№3
Функция получает на вход строку из двух чисел через пробел. 
Сформируйте словарь, где ключом будет символ из Unicode, а значением - целое число. 
Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно"""

def num_unicode(text: str) -> dict[str, int]:

    one, two = map(int, text.split())
    result = {}
    for i in range(min(one, two), max(one, two)+1):
        result[chr(i)] = i
    return(result)

print(num_unicode("12 19"))
"""№4
Функция получает на вход список чисел. 
Отсортируйте его элементы in place без использования встроенных в язык сортировок. 
Как вариант напишите сортировку пузырьком. Её описание есть в википедии."""


def sort_number(a: list) -> None:
    n = 1
    while n < len(a):
        for i in range(len(a) - n):

            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        n +=1
    return a
list_user = list((1, 4, 2, 8, 3, 68, 3, 99))
# sort_number(list_user)
# print(list_user)


"""№5
Функция принимает на вход три списка одинаковой длины:
имена str, 
ставка int, 
премия str с указанием процентов вида “10.25%”.
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии"""

def user_money(names: list[str], salaries: list[int], bonus: list[str]) -> dict[str, float]:


    result = {}
    for n, s, b in zip(names, salaries, bonus):
        result[n] = (s * float(b[:-1])) / 100
    return result




n_1 = ["Иван", "Николай", "Пётр"]
s_1 = [12_000, 96_000, 10_000]
b_1 = ["10.25%", "10.25%", "10.25%"]
# print(user_money(n_1, s_1, b_1))