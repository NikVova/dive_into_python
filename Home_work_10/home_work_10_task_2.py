import json
"""№2
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
Превратите функции в методы класса, а параметры в свойства.
Задачи должны решаться через вызов методов экземпляра."""



"""Напишите функцию, которая создаёт из созданного ранее файла  новый с данными в формате JSON. Имена пишите с большой буквы. 
Каждую пару сохраняйте с новой строки."""

class New_json:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def convert(self):
        dic = {}
        with open(self.file_name, 'r', encoding='utf-8') as f:
            for line in f:
                li = line.split(',')

                dic[li[0].capitalize()] = float(li[1])
        with open('file_json.json', 'w', encoding='utf-8') as f:
            json.dump(dic, f, ensure_ascii=False, indent=2)  # indent=2 перенос на новую строку


file = New_json('new_file.txt')
# file.convert()

"""Напишите функцию, которая в бесконечном цикле запрашивает имя,  личный идентификатор и уровень доступа (от 1 до 7). 
После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени. Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
При перезапуске функции уже записанные в файл данные должны сохраняться. """


class Ident:
    def __init__(self, name_file: str):
        self.name_file = name_file

    def ident(self):
        dic = {}
        second = {}
        with open(self.name_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        dic = data
        print(type(dic))
        print(dic)
        while True:
            name = input("Введите имя: ")
            if name == '':
                break
            id = int(input("Введите личный идентификатор: "))
            lev = input('Введите уровень доступа (от 1 до 7): ')
            second = {id: name}

            if dic.get(lev) is None:
                dic[lev] = second
            else:
                k = dic.get(lev)
                k.update(second)
        with open(self.name_file, 'w', encoding='utf-8') as f:

            json.dump(dic, f, ensure_ascii=False, indent=2)


file = Ident('indent.json')
file.ident()
