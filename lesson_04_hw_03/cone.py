# Завдання 3.
# Написати функцію, яка обчислює площу та об'єм конуса за його радіусом та висотою.
# Функція має повертати два значення.

import math


def cone_square_and_volume(radius, height):
    square = round((math.pi * radius * ((radius + (radius ** 2 + height ** 2)) ** 0.5)), 3)
    volume = round(((1 / 3) * math.pi * (radius ** 2) * height), 3)
    return square, volume


radius_input = float(input('Введить радіус конуса: '))
height_input = float(input('Введить висоту конуса: '))

res = cone_square_and_volume(radius_input, height_input)

print('Площа конуса:', res[0])
print('Об\'єм конуса:', res[1])
