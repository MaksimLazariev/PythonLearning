"""Задача 02"""


# Напишите функцию, которая принимает строку текста. Сформируйте список
# с уникальными кодами Unicode каждого символа введённой строки
# отсортированный по убыванию.


def text_to_ord(my_text: str) -> list[int]:
    """Возвращает список с уникальными кодами Unicode каждого символа"""
    # return sorted(list(set(map(ord, list(my_text)))), reverse = True)

    ord_set = set()
    for i in my_text:
        ord_set.add(ord(i))

    return sorted(list(ord_set), reverse=True)


my_string = input('Введите строку:')
print(text_to_ord(my_string))
