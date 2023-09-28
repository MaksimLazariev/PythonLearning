""" Задача 3 """
# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов, где это возможно

# pylint: disable=C0103

BINARY_DIVIDER: int = 2
OCTAL_DIVIDER: int = 8
STR_CUTTER: int = 2

dividers: list[int] = [BINARY_DIVIDER, OCTAL_DIVIDER]
number: int = int(input("Введите целое число: "))

for divider in dividers:
    temp_number: int = number
    result: str = ""
    while temp_number > 0:
        result = str(temp_number % divider) + result
        temp_number = temp_number // divider

    if result == bin(number)[2:]:
        print(number, result, bin(number))
    elif result == oct(number)[2:]:
        print(number, result, oct(number))
