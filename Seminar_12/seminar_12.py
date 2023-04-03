import json

"""№1
Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и их факториалов."""


class Factorial:
    def __init__(self, k: int):
        self.k = k
        self.val_list = [None] * self.k
        self.key_list = [None] * self.k

    def __call__(self, n: int, *args, **kwds):
        if (n == 1 or n == 0):
            return 1
        result = 1
        for i in range(1, n + 1):
            result = i * result
        self.val_list.append(result)
        self.val_list.pop(0)
        self.key_list.append(n)
        self.key_list.pop(0)
        # print(self.val_list, self.key_list)
        return result

    def view(self):
        return f'{self.val_list} \n {self.key_list}'

    """2"""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('file_factorial.json', 'w', encoding='utf-8') as f:
            slovar = dict(zip(self.key_list, self.val_list))
            json.dump(slovar, f, ensure_ascii=False, indent=2)


# f = Factorial(5)
# with Factorial(5) as f:
#     print(f(6))
#     print(f(7))
#     print(f(8))
#     print(f(5))
#     print(f(4))
#     print(f(3))
#     print(f.view())

"""№2
Доработаем задачу 1. 
Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл."""

"""№3
Создайте класс-генератор. 
Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step. 
Если переданы два параметра, считаем step=1. 
Если передан один параметр, также считаем start=1."""


class MyFac:
    def __init__(self, *args):
        match len(args):
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1
            case 2:
                self.start = args[0]
                self.stop = args[1]
                self.step = 1
            case 3:
                self.start = args[0]
                self.stop = args[1]
                self.step = args[2]

    def __iter__(self):
        return self

    def __next__(self):
        # if(self.start==1 or self.stop==0):
        #      return 1
        while self.start < self.stop:
            result = 1
            for i in range(2, self.start + 1):
                result = i * result
            self.start += self.step
            return result
        raise StopIteration


fib = MyFac(0, 8, 1)
for num in fib:
    print(num)
