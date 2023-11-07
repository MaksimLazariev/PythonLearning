# Напишите программу, которая использует модуль logging для вывода сообщения
# об ошибке в файл. Например, отлавливаем ошибку деления на ноль.

import logging
logging.basicConfig(filename = 'task01.log', filemode='w', encoding='utf-8',
                    level = logging.ERROR)

def get_value(my_dict: dict, key, def_value=None):
    try:
        return my_dict[key]
    except KeyError:
        logging.error(f'Ключ {key} отсутствует в словаре {my_dict}')
        return def_value


if __name__ == '__main__':
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(get_value(my_dict, 'd'))
    print(get_value(my_dict, 'd', 'опять'))