"""Завдання 3.
Дано список з чисел та рядків. Рядки у списку завжди непорожні та складаються тільки з символів 0123456789.
За допомогою функції sorted() отримати копію цього списку:
a) відсортовану за значенням числа елементу."""


def first(elem):
    return float(elem)


my_list = [5, '9', 0, '452', 6.5, '6', 1, 2]

my_list_s = sorted(my_list, key=first)

print(my_list_s)