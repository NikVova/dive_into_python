"""Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной
информации. Также реализуйте возможность запуска из
командной строки с передачей параметров."""
import math
import logging
import argparse

import logging
import argparse

# Создаем объект logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создаем обработчик для вывода логов на консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Создаем обработчик для записи логов в файл
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Rectangle:

    def __init__(self, side_a: float, side_b=None):
        try:
            if side_a <= 0:
                raise ValueError(f'value must be greater than 0')
            else:
                self.side_a = side_a
                if side_b is None:
                    self.side_b = side_a
                elif side_b <= 0:
                    raise ValueError(f'value must be greater than 0')
                else:
                    self.side_b = side_b
        except ValueError as e:
            logger.error(str(e))
            raise

    def square_rectangle(self):
        logger.info('Вычисление площади прямоугольника')
        return self.side_a * self.side_b

    def len_rectangle(self):
        logger.info('Вычисление периметра прямоугольника')
        return (self.side_a + self.side_b) * 2


if __name__ == '__main__':
    # Создаем парсер аргументов командной строки
    parser = argparse.ArgumentParser(description='Вычисление площади и периметра прямоугольника')
    parser.add_argument('a', type=float, help='Длина стороны а')
    parser.add_argument('-b', type=float, help='Длина стороны b')
    args = parser.parse_args()

    # Создаем объект прямоугольника с заданными параметрами
    try:
        rectangle = Rectangle(args.a, args.b)
    except ValueError as e:
        logger.error('Ошибка создания объекта прямоугольника')
        exit(1)

    # Вычисляем площадь и периметр прямоугольника
    try:
        square = rectangle.square_rectangle()
        logger.info(f'Площадь прямоугольника: {square}')
        length = rectangle.len_rectangle()
        logger.info(f'Периметр прямоугольника: {length}')
    except Exception as e:
        logger.error('Ошибка вычисления площади или периметра прямоугольника')
        exit(1)