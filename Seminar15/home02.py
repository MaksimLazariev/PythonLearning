# Создайте класс окружность. Класс должен принимать радиус окружности при
# создании экземпляра. У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

# 1. Добавьте к ним логирование ошибок и полезной информации.
# 2. Также реализуйте возможность запуска из командной строки с передачей параметров

import argparse
import logging
from math import pi

logging.basicConfig(filename = 'home02.log', filemode='w', encoding='utf-8',
                    level = logging.INFO)
logger = logging.getLogger(__name__)

def log_decor(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error((f'Возникла ошибка {e} в функции {func.__name__} с аргументами {args} и {kwargs}'))
            return None
    return wrapper

class Circle:
    PI = pi
    @log_decor
    def __init__(self, radius):
        self.radius = int(radius)

    @log_decor
    def length(self):
        return 2*self.PI*self.radius

    @log_decor
    def square(self):
        return self.PI*self.radius**2

@log_decor
def parser():
    """Добавили парсер"""
    parser = argparse.ArgumentParser(description='circle parser')
    # Добавили тип аргумента и значение по умолчанию
    parser.add_argument('-r','--radius', default = 10)
    args = parser.parse_args()
    return f'{Circle(args.radius).radius = }, {Circle(args.radius).length() = }, {Circle(args.radius).square() = }'


if __name__ == '__main__':
    # Проверка класса Circle через IDE
    # circle01 = Circle(5)
    # print(f'{circle01.radius = }, {circle01.length() = }, {circle01.square() =}')

    # Проверка класса Circle через командную строку
    # python Seminar15/home02.py -r 5

    # Проверка класса Circle через командную строку на ошибку
    # python Seminar15/home02.py -r str

    print(parser())