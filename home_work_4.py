"""№1 Напишите функцию для транспонирования матрицы"""

matr = [[1,2, 3], [4, 5, 6]]

def transpose(list: int) -> list[int]:
    res = []
    n = len(matr)
    m = len(matr[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp+[matr[i][j]]
        res = res+[tmp]
    return res

# print(transpose(matr))

"""№2 Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ - значение переданного аргумента, а значение - имя аргумента. 
Если ключ не хешируем, используйте его строковое представление."""