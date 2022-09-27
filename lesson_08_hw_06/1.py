"""Завдання 1.
Дано довільний список. Створити функцію index(lst, elem), що повертатиме індекс elem в списку lst,
 або, якщо елемент відсутній, то None."""


def index(lst, elem):
    for idx, item in enumerate(lst):
        if item == elem:
            return idx


my_list = [2, 'l', 0, 'you', '70', 12, 0.512, [9, 'b']]
print('Індекс елемента', 12, 'дорівнює', index(my_list, 12))
