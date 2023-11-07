""" Задание №6 """
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, не менее 30 и не более 600 у.е.
# ✔ После каждой 3ей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

DEPOSIT_RATE = 50
WITHDROW_PERCENT = 0.015
LOW_COMMISSION_BORDER = 30
HIGH_COMMISSION_BORDER = 600

INCOME_PERCENT_COUNTER = 3
INCOME_PERCENT = 1.03

RICHNESS = 5_000_000
RICHNESS_PERCENT = 0.9

amount = 1_000_000
operation_count = 0

while True:
    if amount > RICHNESS:
        amount *= RICHNESS_PERCENT
        print('Налог на богатство 10%. Сумма равна ', amount)
    operation_type = input(
        'Введите тип операции, 1 - пополнение, 2 - снятие, 3 - выход: ')
    match operation_type:
        case '1':
            print('1. Операция пополнение счета')
            deposit = int(input('Введите сумму внесения кратно 50: '))
            if deposit % DEPOSIT_RATE == 0:
                amount += deposit
                operation_count += 1
            else:
                print('Операция невыполнима. Сумма должна быть кратна 50')
        case '2':
            print('2. Операция снятие со счета')
            withdrow = int(input('Введите сумму снятия: '))
            if withdrow % DEPOSIT_RATE == 0:
                commission = withdrow * WITHDROW_PERCENT
                if commission < LOW_COMMISSION_BORDER:
                    commission = LOW_COMMISSION_BORDER
                elif commission > HIGH_COMMISSION_BORDER:
                    commission = HIGH_COMMISSION_BORDER
                if amount > withdrow + commission:
                    amount -= withdrow + commission
                operation_count += 1
            else:
                print('Операция невыполнима. Сумма должна быть кратна 50')
        case '3':
            print('3. Выход')
            break
        case _:
            print('Недопустимая операция')
    print("Сумма равна ", amount)
    if operation_count !=0 and operation_count % INCOME_PERCENT_COUNTER == 0:
        amount *= INCOME_PERCENT
        print('Начислены 3%, сумма равна ', amount)
        operation_count = 0
print("Итоговая сумма равна ", amount)
