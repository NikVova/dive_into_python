

def mystery(m:str, answer:list, chanse: int) -> int:

    for i in range(chanse):
        user_answer = (input("Введите ответ: "))
        if user_answer in answer:
            return i + 1
    return 0


if __name__ == '__main__':

    m = print("Зимой и летом одним цветом?")
    res = ['елка', 'лампочка', 'собака']
    ch = 5
    mystery(m, res, ch)