# Завдання 2.
# Написати функцію для рішення квадратних рівнянь.
# Функція має враховувати рішення квадратного рівняння в комплексній площині.
# Тобто з використанням комплексних чисел, квадратне рівняння завжди матиме рішення.

def solve_quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print('Корені рівняння:')
        print(round(x1, 3))
        print(round(x2, 3))
    elif d == 0:
        x1 = -b / (2 * a)
        print('Корінь рівняння: ', round(x1, 3))
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print('Корені рівняння є комплексними числами:')
        print(x1)
        print(x2)


a = float(input('Введить коефіціент а: '))
b = float(input('Введить коефіціент b: '))
c = float(input('Введить коефіціент с: '))

solve_quadratic_equation(a, b, c)


