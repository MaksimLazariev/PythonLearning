"""Задача 2"""
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.

# pylint: disable=C0103

HEX_DIVIDER = 16
STR_CUTTER = 2
# Вводим список с шестнадцатеричными элементами
HEX_NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B',
               'C', 'D', 'E', 'F']

number = int(input('Введите целое число: '))
temp_number = number
result = ""
while temp_number > 0:
    result = HEX_NUMBERS[temp_number % HEX_DIVIDER] + result
    temp_number = temp_number // HEX_DIVIDER

if result == hex(number)[2:]:
    print(number, result, hex(number))
