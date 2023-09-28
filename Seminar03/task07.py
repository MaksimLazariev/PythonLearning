"""Задача 7"""
# Пользователь вводит строку текста. Подсчитайте сколько раз встречается
# каждая буква в строке без использования метода count и с ним. Результат
# сохраните в словаре, где ключ - символ, а значение - частота встречи символа
# в строке. Обратите внимание на порядок ключей. Объясните почему они совпадают
# или не совпадают в ваших решениях.

# pylint: disable=C0103

my_string = 'Пользователь вводит строку текста'
result_dict = {}

for i in my_string:
    result_dict[i] = result_dict.get(i, 0) + 1
print(result_dict)

# for i in my_string:
#     if i not in result_dict:
#         result_dict[i] = my_string.count(i)
# print(result_dict)
