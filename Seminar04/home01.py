"""Задача 01"""
# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def matrix_transposing(my_matrix: list[list[int]]) -> list[list[int]]:
    """Функция транспонирования матрицы"""
    return list(map(list, zip(*my_matrix)))


matrix = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 0]]
print(matrix_transposing(matrix))
