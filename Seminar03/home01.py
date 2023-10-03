"""Задача 1"""
# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.
# [1, 2, 3, 1, 2] -> [1, 2]

my_list = [1, 2, 1, 3, 1, 4, 8, 5, 2, 8, 3, 5, 1, 6]

result_list = []
for i in my_list:
    if my_list.count(i) >= 2 and i not in result_list:
        result_list.append(i)
print('Уникальный список повторяющихся элементов', result_list)

second_result = set()
for i in my_list:
    if my_list.count(i) >= 2:
        second_result.add(i)
print('Уникальный список повторяющихся элементов', list(second_result))
