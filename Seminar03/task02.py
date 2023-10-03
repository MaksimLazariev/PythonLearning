"""Задача 2"""
# Пользователь вводит данные. Сделайте проверку данных и преобразуйте, если
# возможно в один из вариантов ниже:
# целое положительное число,
# вещественное положительное или отрицательное число,
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква,
# строку в верхнем регистре в остальных случаях.

# pylint: disable=C0103

my_string = '-23.45'

if my_string.isdigit():
    print('Положительное целое число:', int(my_string))

elif '.' in my_string:
    minus_flag = False
    if '-' in my_string:
        my_string = my_string.replace('-', '')
        minus_flag = True
    left_part, right_part = my_string.split('.')
    if left_part.isdigit() and right_part.isdigit():
        if minus_flag:
            print('Вещественное отрицательное число:', -float(my_string))
        else:
            print('Вещественное положительное число:', float(my_string))

elif my_string != my_string.lower():
    print('Строка в нижнем регистре', my_string.lower())
else:
    print('Строка в верхнем регистре', my_string.upper())
