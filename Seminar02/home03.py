"""Задача 3"""
# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму
# и произведение дробей. Для проверки своего кода используйте модуль fractions.

# pylint: disable=C0103

from fractions import Fraction

DIVIDER_START = 2
FIRST_ELEMENT = 0
SECOND_ELEMENT = 1

# Вводим дроби в виде строк
str_num01 = '2/21'
str_num02 = '20/5'

# Вычисляем сумму и произведения дробей используя модуль Fraction
fraction_num01 = Fraction(str_num01)
fraction_num02 = Fraction(str_num02)
fraction_result_sum = fraction_num01 + fraction_num02
fraction_result_multiplication = fraction_num01 * fraction_num02
# print(fraction_result_sum, fraction_result_multiplication)

# Находим числитель и знаменатель из строк и записываем в целочисленный список
int_list_num01 = [int(i) for i in str_num01.split('/')]
int_list_num02 = [int(i) for i in str_num02.split('/')]
# print(int_list_num01, int_list_num02)

# Находим числитель и знаменатель суммы дробей
numerator_sum = int_list_num01[FIRST_ELEMENT] * \
                int_list_num02[SECOND_ELEMENT] + \
                int_list_num02[FIRST_ELEMENT] * \
                int_list_num01[SECOND_ELEMENT]
denominator_sum = int_list_num01[SECOND_ELEMENT] * \
                  int_list_num02[SECOND_ELEMENT]
# print(numerator_sum, denominator_sum)

# Находим числитель и знаменатель произведения дробей
numerator_multiplication = int_list_num01[FIRST_ELEMENT] * \
                           int_list_num02[FIRST_ELEMENT]
denominator_multiplication = int_list_num01[SECOND_ELEMENT] * \
                             int_list_num02[SECOND_ELEMENT]

divider = DIVIDER_START
# Находим макс общий делитель числителя и знаменателя суммы дробей
if numerator_sum > denominator_sum:
    max_divider = denominator_sum
else:
    max_divider = numerator_sum
# Сокращаем дробь (сумму дробей)
while divider < max_divider:
    if numerator_sum % divider == 0 and denominator_sum % divider == 0:
        numerator_sum /= divider
        denominator_sum /= divider
    divider += 1
# print(numerator_sum, denominator_sum)

# Записываем результат суммы в строку
str_result_sum = str(int(numerator_sum)) + '/' + str(int(denominator_sum))

divider = DIVIDER_START
# Находим макс общий делитель числителя и знаменателя произведения дробей
if numerator_multiplication > denominator_multiplication:
    max_divider = denominator_multiplication
else:
    max_divider = numerator_multiplication
# Сокращаем дробь (сумму дробей)
while divider < max_divider:
    if numerator_multiplication % divider == 0 and \
            denominator_multiplication % divider == 0:
        numerator_multiplication /= divider
        denominator_multiplication /= divider
    divider += 1
# print(numerator_multiplication, denominator_multiplication)

# Записываем результат произведения в строку
str_result_multiplication = str(int(numerator_multiplication)) + '/' + \
                            str(int(denominator_multiplication))

# проверяем результат суммы
if Fraction(str_result_sum) == fraction_result_sum:
    print('Сумма дробей', str_result_sum, fraction_result_sum)

# проверяем результат произведения
if Fraction(str_result_multiplication) == fraction_result_multiplication:
    print('Произведение дробей', str_result_multiplication,
          fraction_result_multiplication)
