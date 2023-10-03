"""Задача 04"""


# Функция получает на вход список чисел. Отсортируйте его элементы
# in place без использования встроенных в язык сортировок. Как вариант
# напишите сортировку пузырьком. Её описание есть в википедии.

def list_sort(my_list: list[int]):
    """Сортировка пузырьком"""
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if my_list[i] < my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]


task_list = [3, 5, 6, 7, 3, 2, 2, 1, 5]
list_sort(task_list)
print(task_list)
