# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# имя файла без расширения или название каталога,
# расширение, если это файл,
# флаг каталога,
# название родительского каталога.

import pathlib
from pprint import pprint
from collections import namedtuple

DIRSUBJECT = namedtuple('Dirsubject',['filename', 'extention', 'dir_flag', 'parent_name'])

def dir_info(path):
    dir_list = []
    path = pathlib.Path(path)
    for file in path.iterdir():
        dir_list.append(DIRSUBJECT(file.name, file.suffix, file.is_dir(), file.parent))
    return dir_list

if __name__ == '__main__':
    pprint(dir_info(r'C:\Users\Zareff\Desktop\Learning\Python\DeepLearning'))

