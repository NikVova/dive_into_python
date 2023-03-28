from mystery_dict import *

__all__ = ['mystery']


def mystery(num: int) -> str:
    user_num = dict_mystery(int(input("Введите номер загадки от 1 до 7: ")))
    for i in range(num):

        print(user_num[0])
        ans = input("Введите ответ: ").lower()
        if ans == user_num[1]:
            return "Вы угадали!"
        else:
            num: int + 1

    return 0


if __name__ == '__main__':
    print(mystery(int(input("Введите количество попыток: "))))