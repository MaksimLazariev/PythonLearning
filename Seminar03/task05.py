"""Задача 5"""
# Создайте вручную список с повторяющимися целыми числами. Сформируйте список
# с порядковыми номерами нечётных элементов исходного списка. Нумерация
# начинается с единицы.


my_list = [ 1, 2, 1, 3, 1, 4, 5, 8, 2, 8, 3, 1, 6]
result_list = []

for i,j in enumerate(my_list,start=1):
    if j % 2:
        result_list.append(i)

print(result_list)