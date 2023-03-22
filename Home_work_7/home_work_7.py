import os
import shutil
from pathlib import Path


# with (
#     open('text_one.md', 'w', encoding='utf-8') as f1,
#     open('text_two.txt', 'w', encoding='utf-8') as f2,
#     open('text_three.txt', 'w', encoding='utf-8')as f3,
#     open('text_four.txt', 'w', encoding='utf-8')as f4
#     ):
#         f1.write('Hello world!')
#         f2.write('Hello world!')
#         f3.write('Hello world!')
#         f4.write('Hello world!')


def files_rename(new_name: str, ext_old: str, new_ext: str, a, b: int):
    dir_files = os.listdir()
    print(dir_files)
    for i in range(len(dir_files)):
        if ext_old in dir_files[i]:
                cut = dir_files[i][a:b]
                name = (f'{cut}{new_name}{0}{i}{new_ext}')
                os.rename(dir_files[i], name)

files_rename('file','.txt', '.md', 1, 3)
