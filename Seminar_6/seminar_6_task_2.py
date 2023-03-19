import random
from sys import argv

__all__ = ['more_less']


def more_less(down: int = 0, up: int = 100, chanse: int = 5) -> bool:
    num = random.randint(down, up)
    for i in range(chanse):
        print(f"Введите значение от {down} до {up}")
        num_user = int(input())
        if num_user > num:
            print("Загаданное число меньше.")
        elif num_user < num:
            print("Загаданное число , больше.")
        else:
            return True
    return False


if __name__ == '__main__':
    tmp_path, *params = argv
    print(more_less(*(int(n) for n in params)))
    # down = int(input("Нижняя граница: "))
    # up = int(input("Верхняя граница: "))
    # chanse = int(input("Количество попыток: "))
    # print(more_less(down, up, chanse))
