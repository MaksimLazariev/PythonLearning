"""Задача 01"""


# Напишите функцию группового переименования файлов. Она должна:
# 1. + принимать параметр желаемое конечное имя файлов. При переименовании
# в конце имени добавляется порядковый номер.
# 2. + принимать параметр количество цифр в порядковом номере.
# 3. + принимать параметр расширение исходного файла. Переименование должно
# работать только для этих файлов внутри каталога.
# 4. + принимать параметр расширение конечного файла.
# 5. + принимать диапазон сохраняемого оригинального имени. Например, для
# диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним
# прибавляется желаемое конечное имя, если оно передано. Далее счётчик
# файлов и расширение.
# 6. + Отработать отсутствие параметров (пустые значения, либо умолчание)

__all__ = ['group_file_rename', 'specified_number_of_digits']

import os


def group_file_rename(path: str,
                      new_file_name: str = '',          #  по умолч ''
                      number_of_digits: int = 2,
                      replaced_extention: str = '*',    # * - замена всех
                      new_extention: str = '',          # по умолч равно старому расширению
                      original_name_range: list[int] = [0,0], ): # по умолчанию не печатаем старое имя
    """Функция группового переименования файлов"""

    os.chdir(path)  # переходим в папку с файлами замены
    files_list = os.listdir()   # собираем в список все файлы в папке

    counter = 1 # готовим счетчик заменяемых файлов
    start_name_position, stop_name_position = original_name_range # диапазон куска от старого имени
    # Проверка границ диапазона
    if start_name_position > stop_name_position:
        start_name_position, stop_name_position = stop_name_position, start_name_position

    if start_name_position < 0:  # Проверка нижней границы диапазона
        start_name_position = 0

    for _, file in enumerate(files_list): # проходим по списку файлов
        file_name, extention = file.split('.')   # разделяем имя и расширение

        if new_extention == '': # если новое расширение пустое, присваиваем старое расширение
            temp_extention =  extention
        else:
            temp_extention = new_extention

        if stop_name_position > len(file):
            temp_stop_name_position = len(file) - 1
        else:
            temp_stop_name_position = stop_name_position

        # делаем замену в искомом расширении, если *, то замена всех файлов
        if extention == replaced_extention or replaced_extention == '*':
            # собираем новое имя согласно требованиям
            new_file = file_name[start_name_position: temp_stop_name_position] +\
                       new_file_name +\
                       specified_number_of_digits(number_of_digits, counter) +\
                       '.' + temp_extention
            counter += 1
            os.rename(file, new_file)   # делаем переименование

def specified_number_of_digits(digits: int, counter: int) -> str:
    """Функция печатает число с заданным количеством знаков (5, 15) -> 00015"""
    counter = str(counter)
    for _ in range(len(str(counter)),digits):
        counter = '0' + counter
    return counter


if __name__ == '__main__':
    group_file_rename(r'test02', '_new_', 4, 'mov', 'mr1', [3, 6])

    # group_file_rename(r'test02', 'file', 2, '*'])

    # group_file_rename(r'test02', '', 2)
     #  f.exe       ->  01.exe
     #  f.mov       ->  02.mov
     #  file333.txt ->  le03.txt
     #  file22.mov  ->  le04.mov
