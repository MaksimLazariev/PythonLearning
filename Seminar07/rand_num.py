"""Задача01"""
# Напишите функцию, которая заполняет файл (добавляет в конец) случайными
# парами чисел. Первое число int, второе - float разделены вертикальной
# чертой. Минимальное число - -1000, максимальное - +1000. Количество строк
# и имя файла передаются как аргументы функции.

__all__ = ['rand_num']

from random import randint, uniform

LOWBORDER = -1000
HIGHBORDER = 1000


def rand_num(count, file_name):
    """Генерация целого и вещественного чисел"""
    with open(file_name, "w", encoding="utf-8") as f:
        for _ in range(count):
            f.write(
                f'{randint(LOWBORDER, HIGHBORDER)}|{uniform(LOWBORDER, HIGHBORDER)}\n')


if __name__ == '__main__':
    NUMBER_OF_NUMBERS = 10
    rand_num(NUMBER_OF_NUMBERS, 'test01.py')
