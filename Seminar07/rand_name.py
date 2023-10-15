"""Задача 02"""
# Напишите функцию, которая генерирует псевдоимена. Имя должно начинаться
# с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны
# быть гласные. Полученные имена сохраните в файл.

__all__ = ['rand_name', 'rnd_name_in_file']

from random import randint

MIN_LENGTH = 4
MAX_LENGTH = 4
LOWER_A = 97
LOWER_Z = 122
VOVELS = "eyioau"


def rand_name(min_length: int = MIN_LENGTH,
              max_length: int = MAX_LENGTH) -> str:
    """Генерация рандомного слова"""
    name_len = randint(min_length, max_length)
    while True:
        name = ''
        for i in range(name_len):
            name += chr(randint(LOWER_A, LOWER_A))
        for i in name:
            if i in VOVELS:
                return name.capitalize()


def rnd_name_in_file(count, file_name):
    """Запись слова в файл"""
    with open(file_name, "w") as f:
        for _ in range(count):
            f.write(f'{rand_name()}\n')


if __name__ == '__main__':
    NUMBER_OF_WORDS = 10
    rnd_name_in_file(NUMBER_OF_WORDS, 'test02.py')
