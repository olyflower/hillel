"""Завдання 2.
Створити функцію copydeep(lst), що створює глибоку копію довільного списку. Умови:
Не можна використовувати deepcopy з модулю copy
Якщо редагується будь-яка частина чи вкладений на довільній глибині елемент оригінального списку,
то в копії не має нічого змінюватися.
lst1 = ['a', 1, 2.0, ['b']]
lst2 = copydeep(lst1)
lst1[3].append(0)
print(lst1[3], lst2[3])  # ['b', 0] ['b']"""


def copy_deep(lst):
    if isinstance(lst, list):
        return list(map(copy_deep, lst))
    return lst


my_list = ['a', 1, 2.0, ['b']]
list_copy = copy_deep(my_list)
my_list[3].append('0')
print(my_list[3], list_copy[3])
