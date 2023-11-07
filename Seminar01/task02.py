# Пользователь вводит число от 1 до 999.
# Используя операции с числами сообщите что введено:
# цифра, двузначное число или трёхзначное число.
#
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
#
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

ONE_DIGIT_LOW_BORDER = 1
ONE_DIGIT_HIGH_BORDER = TWO_DIGIT_LOW_BORDER = 10
TWO_DIGIT_HIGH_BORDER = THREE_DIGIT_LOW_BORDER = 100
THREE_DIGIT_HIGH_BORDER = 1000

number = int(input('Введите число от 1 до 999: '))
digit = None
result = -1

match number:
    case num if ONE_DIGIT_LOW_BORDER <= num < ONE_DIGIT_HIGH_BORDER:
        digit = 1
        result = num ** 2
    case num if TWO_DIGIT_LOW_BORDER <= num < TWO_DIGIT_HIGH_BORDER:
        digit = 2
        result = (num // TWO_DIGIT_LOW_BORDER) * (num % ONE_DIGIT_HIGH_BORDER)
    case num if THREE_DIGIT_LOW_BORDER <= num < THREE_DIGIT_HIGH_BORDER:
        digit = 3
        result = (num // THREE_DIGIT_LOW_BORDER) + \
                 ((num % THREE_DIGIT_LOW_BORDER) - (
                         num % ONE_DIGIT_HIGH_BORDER)) + \
                 ((num % ONE_DIGIT_HIGH_BORDER) * THREE_DIGIT_LOW_BORDER)

if result > 0:
    print('Число {} {}-разрядное, результат равен {}'.format(number, digit,
                                                             result))
else:
    print('Число введено неверно')
