import re

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
print(duplicate_num(list_1))

"""№2
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых . 
Не учитывать знаки препинания и регистр символов . За основу возьмите любую статью из википедии
или из документации к языку."""

def read_str(a: str) -> None:
    str = input('Введите строку: ')
    print()
    a = re.sub(r'[^\w\s]', '', str)
    a = sorted(set(a.lower().split()), key=a.count, reverse=True)
    return (a)

print(*(read_str(str))[:10], sep='\n')

"""№3
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант."""

def backpack(a: int) -> list [str]:


    volume_backpack = int(input('Введите объем рюкзака: '))
    things_backpack = {'зажигалка': 2, 'компас': 5, 'фрукты': 10, 'рубашка': 4,
      	'термос': 5, 'аптечка': 7, 'куртка': 6, 'бинокль': 4, 'удочка': 3,
          'салфетки': 2, 'бутерброды': 10, 'палатка': 12, 'спальный мешок': 8, 'жвачка': 1}
    res = list()
    for k, v in things_backpack.items():
        if v <= volume_backpack:
            res.append(k)
            volume_backpack -= v
    return res
print(*(backpack(a=0)), sep='\n')

