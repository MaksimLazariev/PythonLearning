"""Задача 05"""


# Функция принимает на вход три списка одинаковой длины: имена str,
# ставка int, премия str с указанием процентов вида “10.25%”.
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве
# значения. Сумма рассчитывается как ставка умноженная на процент премии

def bonus_dict(names: list[str], salaries: list[int], bonuses: list[int]) -> \
dict[float]:
    my_dict = {}
    for name, salary, bonus in zip(names, salaries, bonuses):
        my_dict[name] = salary * float(bonus[:-1]) / 100
    return my_dict

names = ["Иван", "Николай", "Пётр", "Харитон"]
salaries = [125_000, 96_000, 109_000, 100_000]
bonuses = ['10%', '25.5%', '13.3%', '42.73%']
print(bonus_dict(names, salaries, bonuses))