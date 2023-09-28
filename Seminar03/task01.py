"""Задача 1"""
# Вручную создайте список с целыми числами, которые повторяются. Получите
# новый список, который содержит уникальные (без повтора) элементы исходного
# списка. # *Подготовьте два решения, короткое и длинное, которое не использует
# другие коллекции помимо списков.

# pylint: disable=C0103

my_list = [3, 4, 5, 5, 4, 2, 3, 6, 7]
res_list = []

for element in my_list:
    if element not in res_list:
        res_list.append(element)
print(res_list)

res_set = set(my_list)
print(list(res_set))
