# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# Напишите преобразование в одну строку.

import argparse
import logging

# Инициализация логгера
logging.basicConfig(filename = 'home03.log', filemode='w', encoding='utf-8',
                    level = logging.INFO)
logger = logging.getLogger(__name__)

# Заводим логгер ак декоратор
def log_decor(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error((f'Возникла ошибка {e} в функции {func.__name__} с аргументами {args} и {kwargs}'))
            return None
    return wrapper

@log_decor
def parser():
    """Добавили парсер"""
    parser = argparse.ArgumentParser(description='dict parser')
    # Добавили тип аргумента и значение по умолчанию
    parser.add_argument('-s','--string', nargs='*', default = "Саладин, почти король, которому удалось объединить")
    args = parser.parse_args()
    return f'{str_to_dict(args.string)}'
    # return f'{str_to_dict(args)}'

@log_decor
def str_to_dict(my_lst):
    my_string =' '.join(my_lst)
    my_dict = {i:ord(i) for i in my_string}
    return my_dict

if __name__ == '__main__':
    # Проверка метода str_to_dict через IDE
    # string = "Саладин, почти король, которому удалось объединить"
    # print(str_to_dict(string))

    # Проверка метода str_to_dict через командную строку
    # python Seminar15/home02.py -r Саладин почти король
    print(parser())