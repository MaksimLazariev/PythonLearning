"""Задача 07"""
# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная - ложь.


def company(companies: dict[str, int| float]) -> bool:
    for key, value in companies.items():
        if sum(value) < 0:
            return False
    return True

def is_profit(companys: dict[str, int | float]) -> bool:
    return all(map(lambda x: sum(x) > 0, companys.values()))

data = {
"Рога": [42, 73, 12, 85, -15, 2],
"Копыта": [45, 25, 100, 22, 1],
"Хвосты": [-50, 123, 52, 45, 93],
}
print(company(data))
print(is_profit(data))