"""Завдання №1
Написати функцію, яка буде переводити градуси в радіани (без використання math.radians).
Використовуючи цю функцію, вивести на екран значення косинусів кутів 60, 45 та 40 градусів."""

import math


def degrees2radians(degrees):
    return (degrees * math.pi) / 180


print('Косинус кута 60 градусів:', round(math.cos(degrees2radians(60)), 4))
print('Косинус кута 45 градусів:', round(math.cos(degrees2radians(45)), 4))
print('Косинус кута 40 градусів:', round(math.cos(degrees2radians(40)), 4))
