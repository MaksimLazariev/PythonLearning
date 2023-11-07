# На семинаре про декораторы был создан логирующих декоратор. Он сохранял
# аргументы функции и результат её работы в файл. Напишите аналогичный декоратор,
# но внутри используйте модуль logging.

# Доработаем задачу 2. Сохраняйте в лог файл раздельно: уровень логирования,
# дату события, имя функции (не декоратора), аргументы вызова, результат.

import logging

FORMAT = '{levelname}, {asctime}, {msg}'
logging.basicConfig(format = FORMAT, style= '{',
                    filename = 'task02.log', filemode='w',
                    encoding='utf-8',
                    level = logging.ERROR)
logger = logging.getLogger(__name__)

def log_decor(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error((f'Возникла ошибка {e} в функции {func.__name__} с аргументами {args} и {kwargs}'))
            return None
    return wrapper

@log_decor
def get_value(my_dict: dict, key, def_value=None):
    return my_dict[key]

@log_decor
def div_func(a, b):
    return a/0

if __name__ == '__main__':
    div = div_func(5, 0)
    # my_dict = {'a': 1, 'b': 2, 'c': 3}
    # print(get_value(my_dict, 'd'))
