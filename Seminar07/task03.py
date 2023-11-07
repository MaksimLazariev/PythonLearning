"""Задача 03"""
# Напишите функцию, которая открывает на чтение созданные в прошлых задачах
# файлы с числами и именами. Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
#  - если результат умножения отрицательный, сохраните имя записанное строчными
# буквами и произведение по модулю
#  - если результат умножения положительный, сохраните имя прописными буквами
#  и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном
# файле. При достижении конца более короткого файла, возвращайтесь в его
# начало.

# pylint: disable=C0103

__all__ = ['len_list', 'open_file']

from rand_name import rnd_name_in_file
from rand_num import rand_num


def len_list(list01, list02):
    """Удлинение одного листа до длины второго"""
    # из-за переноса строки в конце файлов сбивается весь порядок, убираем их
    list01.pop()
    list02.pop()
    if len(list01) > len(list02):
        min_len_list = len(list02)
        for i in range(min_len_list - 1, len(list01)):
            list02.append(list02[i % min_len_list])
    elif len(list02) > len(list01):
        min_len_list = len(list01)
        for i in range(min_len_list - 1, len(list02)):
            list01.append(list01[i % min_len_list])
    return list01, list02


def open_file(names_file, num_file, result_file):
    """Чтение данных из двух файлов и запись согласно требованиям в третий """
    with(
        open(names_file, 'r') as ns_f,
        open(num_file, 'r') as nm_f,
        open(result_file, 'w') as r_f):
        names_list = ns_f.read().split('\n')
        nums_list = nm_f.read().split('\n')
        for name, num in zip(*len_list(names_list, nums_list)):
            first_num, second_num = map(float, num.split('|'))
            result = first_num * second_num
            if result < 0:
                r_f.write(f'{name.lower()}, {abs(result)}\n')
            elif result > 0:
                r_f.write(f'{name.upper()}, {int(result)}\n')


if __name__ == '__main__':
    # list01 = [1, 2, 3]
    # list02 = [3, 4, 5, 6, 7, 8, 9]
    # print(len_list(list01, list02))

    NAMES = 10
    NUMBERS = 3

    file01 = 'test01.py'
    file02 = 'test02.py'
    file03 = 'test03.py'

    rnd_name_in_file(NAMES, file01)
    rand_num(NUMBERS, file02)
    open_file(file01, file02, file03)
