import os
import json
import csv
import pickle

"""№1
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.
-   Для дочерних объектов указывайте родительскую директорию.
-   Для каждого объекта укажите файл это или директория.
-   Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""

path = 'D:\Разраб\ПВП\dive_into_python\Папка_1\Папка_2\Папка_4'


def dir_files(path):
    root_dir = { }
    a = os.listdir(path)
    for i in os.listdir(path):
        result = []
        root_dir[i] = result
        print('Обьект: ', i, 'Родительская директория: ', path + '\\' + i)
        if os.path.isdir(path + '\\' + i):
            total_size = 0
            way, dirs, files = next(os.walk(path))
            for f in files:
                fp = os.path.join(path, f)
                total_size += fp.__sizeof__()
            result.append(f'"Это директория. Размер файлов в директории с учётом всех вложенных файлов и директорий: "{total_size}"Количество подкаталогов: " {len(dirs)} "Количество файлов: ", {len(files)}')

        elif os.path.isfile(path + '\\' + i):
            result.append(f'"Это файл. Размер файла байт: "{i.__sizeof__()}')
    # json
    with open('data_dir.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(root_dir, indent=2, ensure_ascii=False))
    # csv
    b = str(root_dir).split('\n')
    with open('data_dir.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, dialect='excel', delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(b)

    # pickle
    with open('data_dir.pickle', 'wb') as f:
        pickle.dump(root_dir, f)


dir_files(path)
s = ''

s.