# Нарисовать в консоли ёлку спросив у пользователя количество рядов.
#
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

STAR = '*'
SPACE = ' '
STAR_MULTIPLIER = 2
ONE_SYMBOL = 1

rows = int(input('Введите количество рядов: '))
for row in range(rows):
    print(SPACE * (rows - row - ONE_SYMBOL) + STAR * (
                row * STAR_MULTIPLIER + ONE_SYMBOL))
