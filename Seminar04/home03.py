"""Задача 03"""
# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции
# функции. Дополнительно сохраняйте все операции поступления и снятия средств
# в список.

# pylint: disable=C0103


def richness_tax():
    """Функция налога на богатство"""
    if operation_list[LAST_BALANCE] > RICHNESS:
        operation_list.append(
            count_percents(operation_list[LAST_BALANCE], RICHNESS_PERCENT))
        print('Налог на богатство 10%. Сумма равна ',
              operation_list[LAST_BALANCE])


def accrual_percents():
    """Функция начисления процентов за количество операций"""
    global counter
    if counter != 0 and counter % INCOME_PERCENT_COUNTER == 0:
        operation_list.append(
            count_percents(operation_list[LAST_BALANCE], INCOME_PERCENT))
        print('Начислены 3%, сумма равна ', operation_list[LAST_BALANCE])
        counter = 0


def count_percents(balance: int | float, percent: float) -> float:
    """Функция расчета процентов"""
    return round(balance * percent, 2)


def income_funds():
    """Функция пополнения счета"""
    global counter
    income_sum = int(input('Введите сумму внесения кратно 50: '))
    if income_sum % DEPOSIT_RATE == 0:
        counter += 1
        operation_list.append(operation_list[LAST_BALANCE] + income_sum)
        # operation_list.append(balance)
    else:
        print('Операция невыполнима. Сумма должна быть кратна 50')


def withdrawal_funds():
    """Функция снятия со счета"""
    global counter
    withdrow = int(input('Введите сумму снятия: '))
    if withdrow % DEPOSIT_RATE == 0:
        commission = withdrow * WITHDROW_PERCENT
        if commission < LOW_COMMISSION_BORDER:
            commission = LOW_COMMISSION_BORDER
        elif commission > HIGH_COMMISSION_BORDER:
            commission = HIGH_COMMISSION_BORDER
        if operation_list[LAST_BALANCE] > withdrow + commission:
            operation_list.append(
                operation_list[LAST_BALANCE] - withdrow - commission)
        counter += 1
        # operation_list.append(balance)
    else:
        print('Операция невыполнима. Сумма должна быть кратна 50')


def atm_machine():
    """Функция банкомата"""
    while True:
        # проверяем налог на богатство
        richness_tax()
        operation_type = input(
            'Введите тип операции, 1 - пополнение, 2 - снятие, 3 - выход: ')
        match operation_type:
            case '1':
                print('1. Операция пополнение счета')
                # Функция пополнения счета
                income_funds()
            case '2':
                #  Функция снятия со счета
                print('2. Операция снятие со счета')
                withdrawal_funds()
            case '3':
                print('3. Выход')
                break
            case _:
                print('Недопустимая операция')
        print("Баланс равен", operation_list[LAST_BALANCE])
        #  проверяем начисление процентов по количеству операций
        accrual_percents()


DEPOSIT_RATE = 50
WITHDROW_PERCENT = 0.015
LOW_COMMISSION_BORDER = 30
HIGH_COMMISSION_BORDER = 600

INCOME_PERCENT_COUNTER = 3
INCOME_PERCENT = 1.03

RICHNESS = 5_000_000
RICHNESS_PERCENT = 0.9

LAST_BALANCE = -1

# основная программа
start_balance = 1_000_000
operation_list: list[int | float] = [start_balance]
counter = 0
print("Итоговая сумма равна ", operation_list[LAST_BALANCE])
print("Список операций", operation_list)
