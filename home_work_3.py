# № 1
# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
def duplicate_num(list: int) -> list[int]:
    """Создает новый список дубликатов без повторений"""

    list_2 = []
    for item in list_1:
        if list_1.count(item) > 1 and item not in list_2:
            for i in range(list_1.count(item)):
                if item not in list_2:
                    list_2.append(item)
    return list_2

list_1 = [1, 2, 3, 2, 5, 1, 6, 2, 4, 1, 5, 8, 7, 9, 7, 0]
# print(duplicate_num(list_1))
