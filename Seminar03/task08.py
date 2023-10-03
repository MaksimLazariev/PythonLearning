"""Задача 8"""
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга,
# а значение - кортеж вещей. Ответьте на вопросы:
# 1. какие вещи взяли все три друга
# 2. какие вещи уникальны, есть только у одного друга
# 3. какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь
# отсутствует
#
# Для решения используйте операции с множествами. Код должен расширяться
# на любое большее количество друзей.

# pylint: disable=C0103

hike = {
    'Aaz': ("спички", "дрова", "топор", "еда"),
    'Skeeve': ("спальник", "спички", "вода", "еда"),
    'Tananda': ("вода", "косметичка", "еда"),
    'Tanan': ("вода", "спички", "косметичка"),
}

result01 = set()
for i in hike.values():
    if result01 == set():
        result01 = set(i)
    else:
        result01 &= set(i)
print('вещи взяли все три друга', result01)

result02 = {}
for key, value in hike.items():
    only_one = set(value)
    for j in hike.values():
        if value != j:
            only_one -= set(j)
    result02[key] = only_one

print('вещи уникальны, есть только у одного друга', result02)

result03 = {}

for key, value in hike.items():
    for element in hike.values():
        not_one = None
        if value == element:
            continue
        elif not not_one and not_one != set():
            not_one = set(element)
        else:
            not_one &= set(element)
    # print(not_one, value, j, not_one - set(value))
    result03[key] = not_one - set(value)

print('вещи есть у всех друзей кроме одного', result03)
