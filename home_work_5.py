
"""№1
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""
def file_path(text: str) -> tuple[str, str, str]:
    data = text.replace('.', '\\').split('\\')
    len_str = text.rfind('\\')
    *a, b, c = data
    result = (text[:len_str + 1], b, c)
    return result

# print(file_path('D:\Семинар\Лекции\волшебник\Дед мороз.jpeg'))


"""№2
Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии 
"""
# def user_money(names: list[str], salaries: list[int], bonus: list[str]) -> dict[str, float]:
#
#     # result = dict(zip(names, bonus) bonus = list(map(float(bonus[:-1]), bonus)))
#     # return result
#
# names = ["Иван", "Николай", "Пётр"]
# salaries = [12_000, 96_000, 10_000]
# bonus = ["10.25%", "10.25%", "10.25%"]
#
#
#
# # print(user_money(names, salaries, bonus))
"""№3
Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""

def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

# for fib in fibonacci(20):
#     print(fib, end=' ')
print(*fibonacci(10))