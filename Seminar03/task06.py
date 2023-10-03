"""Задача 6"""
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировке Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного слова был
# один пробел между ним и номером строки

# pylint: disable=C0103

my_string = input('Введите строку:')
my_list = sorted(my_string.split())

max_word_length = 0
for i in my_list:
    if max_word_length < len(i):
        max_word_length = len(i)
# max_len = len(max(my_list, key = len)) # Находим макс по длине слово в
# списке, и затем находим его длину

for i, j in enumerate(my_list, start=1):
    print(f'{i} {j:>{max_word_length}}')
