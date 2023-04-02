"""№1
Доработаем задачи 5. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""


class Fauna:

    def __init__(self, name: str, blood_color: str):
        self.name = name
        self.blood_color = blood_color

    def eat(self):
        print(' Need food')


class Birds(Fauna):
    def __init__(self, name: str, blood_color: str, feathers: bool):
        super().__init__(name, blood_color)
        self.feathers = feathers

    def fly(self):
        print('I can fly!')


class Fishes(Fauna):
    def __init__(self, name: str, blood_color: str, gills: bool):
        super().__init__(name, blood_color)
        self.gills = gills


class Reptiles(Fauna):
    def __init__(self, name: str, blood_color: str, scales: bool):
        super().__init__(name, blood_color)
        self.scales = scales


class Factory:

    def __init__(self, name, *args):
        self.name = name
        self.args = args
        self.instance = self.__create_instance()

    def __create_instance(self):
        instance = globals()[self.name](*self.args)
        return instance

    def get_attributes(self):
        return self.instance


if __name__ == '__main__':
    a = Factory('Birds', 'Кеша', 'red', True).instance
    print(a)
    print(a.name)
    a.eat()
    a.fly()
