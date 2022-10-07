"""Завдання 2.
Написати функцію для рішення квадратних рівнянь."""


def solve_quadratic_equation(a, b, c):
    x1 = None
    x2 = None
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        x1 = -b / (2 * a)

    return x1, x2


a = float(input('Введить коефіціент а: '))
b = float(input('Введить коефіціент b: '))
c = float(input('Введить коефіціент с: '))

res = solve_quadratic_equation(a, b, c)

if res[0] is None and res[1] is None:
    print('Немає рішень')
elif res[1] is None:
    print('Корінь рівняння:', round(res[0], 3))
else:
    print('Корені рівняння:')
    print(round(res[0], 3))
    print(round(res[1], 3))
