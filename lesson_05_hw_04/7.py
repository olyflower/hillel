"""Завдання 7.
Шаховий кінь ходить буквою "Г" - на дві клітинки по вертикалі в будь-якому напрямку і
на одну клітинку по горизонталі, чи навпаки. Дані дві різні клітини шахівниці,
визначте, чи може кінь потрапити з першої клітини на другу одним ходом.
Клітина шахівниці задається одним рядком, що складається з символу a-h та цифри 1-8: a2, e2, e4, h7, d1, і т.і."""

start = input('Введить клітину, на якій стоїть кінь: ')
x1 = ord(start[0]) - 96
y1 = int(start[1])

target = input('Введить клітину, на яку треба перемістити коня: ')
x2 = ord(target[0]) - 96
y2 = int(target[1])

d_x = abs(x1 - x2)
d_y = abs(y1 - y2)
if d_x == 1 and d_y == 2 or d_x == 2 and d_y == 1:
    print('Кінь може переміститися на дану клітину за один ход')
else:
    print('Кінь не може переміститися на дану клітину за один ход')
