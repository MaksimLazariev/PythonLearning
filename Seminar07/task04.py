"""Задача 04"""

# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# 1. расширение
# 2. минимальная длина случайно сгенерированного имени, по умолчанию 6
# 3. максимальная длина случайно сгенерированного имени, по умолчанию 30
# 4. минимальное число случайных байт, записанных в файл, по умолчанию 256
# 5. максимальное число случайных байт, записанных в файл, по умолчанию 4096
# 6 количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

__all__ = ['create_file', 'generate_files']

from random import randint
from rand_name import rand_name


def create_file(extention, min_name_length=6, max_name_length=30,
                min_file_size=256, max_file_size=4096, number_of_files=4):
    """Функция генерирует новые файлы согласно заданным аргументам"""
    for _ in range(number_of_files):
        file_name = rand_name(min_name_length, max_name_length) + extention
        with open(file_name, 'w') as f:
            f.write(str(bytes([randint(0, 255) for _ in
                               range(randint(min_file_size, max_file_size))])))


def generate_files(ext_list: list[str], num_of_files: int = 5):
    """Функция генерирует файлы с разными расширениями"""
    while num_of_files > 0:
        rand_ext = ext_list[randint(0, len(ext_list) - 1)]
        rand_num_of_files = randint(1, num_of_files)
        # print(f'{rand_ext} / {rand_num_of_files}')
        create_file(rand_ext, number_of_files=rand_num_of_files)
        num_of_files -= rand_num_of_files


if __name__ == '__main__':
    # Проверка генератора файлов по расширению
    # create_file('.r1')
    # Проверка генератора файлов по списку
    list01 = ['.r1', '.s23', '.q5', '.m10', '.f5']
    generate_files(list01)

