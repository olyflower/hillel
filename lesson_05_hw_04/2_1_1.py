# Завдання 2.
# Написати функцію для рішення квадратних рівнянь.
# Функція має враховувати рішення квадратного рівняння в комплексній площині.
# Тобто з використанням комплексних чисел, квадратне рівняння завжди матиме рішення.

def solve_quadratic_equation(a, b, c):
    x2 = None
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)

    return d, x1, x2


a = float(input('Введить коефіціент а: '))
b = float(input('Введить коефіціент b: '))
c = float(input('Введить коефіціент с: '))

res = solve_quadratic_equation(a, b, c)

if res[0] < 0:
    print('Корені рівняння є комплексними числами:')
    print(round(res[1].real, 2) + round(res[1].imag, 2) * 1j)
    print(round(res[2].real, 2) + round(res[2].imag, 2) * 1j)
elif res[0] == 0 and res[1] is None:
    print('Корінь рівняння: ', round(res[2], 3))
elif res[0] == 0 and res[2] is None:
    print('Корінь рівняння: ', round(res[1], 3))
else:
    print('Корені рівняння:')
    print(round(res[1], 3))
    print(round(res[2], 3))
