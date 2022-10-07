"""Завдання 1.
Розширити функцію copydeep() з попереднього домашнього завдання, щоб вона також правильно копіювала tuple та dict."""


def copydeep(value):
    if isinstance(value, list):
        return list(map(copydeep, value))
    elif isinstance(value, tuple):
        return tuple(map(copydeep, value))
    elif isinstance(value, dict):
        return dict(zip(value.keys(), list(map(copydeep, value.values()))))
    return value


my_list = ['a', 1, ['b'], (1, 2, 3), {'Student1': ['Helen', 6], 'Student2': ['1', 6]}]
list_copy = copydeep(my_list)
print(list_copy)
list_copy[-1]['Student1'][1] = 7
print(my_list)
print(list_copy)
