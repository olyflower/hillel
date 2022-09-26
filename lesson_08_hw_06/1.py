"""Завдання 1.
Дано довільний список. Створити функцію index(lst, elem), що повертатиме індекс elem в списку lst,
 або, якщо елемент відсутній, то None."""


def index(lst, elem):
    lst = list(map(str, lst))
    if elem not in lst:
        return None
    for idx, item in enumerate(lst):
        if item == elem:
            return idx


my_list = [2, 'l', 0, 'you', '70', 12, 0.512, [9, 'b']]
print(my_list)
my_elem = input('Введить елемент: ')
print('Індекс елемента', my_elem, 'дорівнює', index(my_list, my_elem))
