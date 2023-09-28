"""Задача 4"""
# Создайте вручную список с повторяющимися элементами. Удалите из него
# все элементы, которые встречаются дважды.

my_list = [1, 2, 1, 3, 1, 4, 5, 8, 2, 8, 3, 1, 6]
for i in set(my_list):
    if my_list.count(i) == 2:
        my_list.remove(i)
        my_list.remove(i)
print(my_list)
