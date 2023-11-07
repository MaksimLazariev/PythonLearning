"""Задача 05"""
# Создайте функцию для сортировки файлов по директориям: видео, изображения,
# текст и т.п. Каждая группа включает файлы с несколькими расширениями. В
# исходной папке должны остаться только те файлы, которые не подошли для
# сортировки.

__all__ = ['sort_files']

import os


# def sort_files(path):
#     os.chdir(path)
#
#     ext_dict = {}
#     for file in path.iterdir():
#         if file.is_file():
#
#             ext_dict[file.suffix] = ext_dict.get(file.suffix,[]) + [file]
#     for key, value in ext_dict.items():
#         os.mkdir(key)
#         for file in value:
#             try:
#                 file.replace(path/key/file.name )
#             except PermissionError:
#                 continue
#
#
# if __name__ == '__main__':
#     sort_files(pathlib.Path(r"C:\Users\Zareff\Desktop\Learning\Python\DeepLearning\Seminar07\test"))


def sort_files(path):
    os.chdir(path)
    files_list = os.listdir()
    ext_dict = {}
    for file in files_list:
        *_, ext = file.split('.')
        ext_dict[ext] = ext_dict.get(ext, []) + [file]

    for key, value in ext_dict.items():
        os.mkdir(key)
        for i in value:
            print(f"{key}, {i}, {key}\\{i}")
            os.replace(i, f"{key}\\{i}")


if __name__ == '__main__':
    sort_files(r"test")
