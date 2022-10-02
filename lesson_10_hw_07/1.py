"""Завдання 1.
Розширити функцію copydeep() з попереднього домашнього завдання, щоб вона також правильно копіювала tuple та dict."""


def copy_deep(lst):
    if isinstance(lst, list):
        return list(map(copy_deep, lst))
    elif isinstance(lst, tuple):
        return tuple(map(copy_deep, lst))
    elif isinstance(lst, dict):
        return dict(zip(lst.keys(), list(map(copy_deep, lst.values()))))
    return lst


my_list = ['a', 1, ['b'], (1, 2, 3), {'Student1': ['Helen', 6], 'Student2': ['1', 6]}]
list_copy = copy_deep(my_list)
print(list_copy)
list_copy[-1]['Student1'][1] = 7
print(my_list)
print(list_copy)
