"""Задача 06"""
# Функция получает на вход список чисел и два индекса. Вернуть сумму чисел
# между переданными индексами. Если индекс выходит за пределы списка, сумма
# считается до конца и/или начала списка. Если нижняя граница меньше нуля,
# суммируем от начала. Если верхняя граница больше длины списка, до конца.


def list_sum(numbers: list[int], start: int, stop: int) -> int:
    if start > stop:
        stop, start = start, stop
    if start < 0 or start > len(numbers):
        start = 0
    if stop > len(numbers) or stop < 0:
        stop = len(numbers)
    return sum(numbers[start:stop])

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(list_sum(numbers, -3, 1))