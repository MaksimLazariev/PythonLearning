"""Задача 03"""
# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def make_dict(my_str: str) -> dict[str, int]:
    start, stop = map(int, my_str.split())
    my_dict = {}
    for i in range (start, stop):
        my_dict[chr(i)] = i
    return my_dict

my_string = input('Введите 2 числа: ')
print(make_dict(my_string))