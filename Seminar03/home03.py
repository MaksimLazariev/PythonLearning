"""Задача 3"""
# Создайте словарь со списком вещей для похода в качестве ключа и их массой
# в качестве значения. Определите какие вещи влезут в рюкзак, передав его
# максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

# pylint: disable=C0103

my_backpack = {"вилка": 1,
               "ложка": 1,
               "вода": 3,
               "ботинки": 3,
               "куртка": 5,
               "камера": 4,
               "чайник": 4,
               "палатка": 12,
               "еда": 5,
               "джинсы": 4,
               "посуда": 2,
               }

BACKPACK_SIZE = 20
count_size = 0
result_dict = {}
# Сортируем словарь по убыванию
sorted_backpack = dict(
    sorted(my_backpack.items(), key=lambda x: x[1], reverse=True))
# Набираем в словарь вещи, пока рюкзак не станет полным
for thing, weight in sorted_backpack.items():
    if count_size + weight <= BACKPACK_SIZE:
        result_dict[thing] = weight
        count_size += weight

print(f'Вещи, которые влезли в рюкзак: {result_dict}, общий вес {count_size}')
