"""Задача 3"""
# Создайте вручную кортеж содержащий элементы разных типов. Получите из него
# словарь списков, где ключ - тип элемента, а значение - список элементов
# данного типа.

my_tuple = (1, 3, 5, 'one', 'two', 'three', True, 3.14, (2, 3))
result_dict = {}

for i in my_tuple:
    result_dict[type(i)] = result_dict.get(type(i), []) + [i]
    # result_dict[type(i)].append(i)

print(result_dict)
