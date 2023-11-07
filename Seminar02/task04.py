"""Задача 4"""
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import decimal
import math

MAX_VALUE_OF_DIAMETER = 1000
decimal.getcontext().prec = 42
PI = decimal.Decimal(math.pi)

diameter = decimal.Decimal(input("Введите диаметр: "))
if diameter < MAX_VALUE_OF_DIAMETER:
    print('Диаметр равен', PI * diameter ** 2 / 4)
    print('Длина равна', PI * diameter)
else:
    print("Введено большое значение")
