"""Завдання 3_1.
Написати програму, що перетворює значення рядкової змінної з формату snake_case
в формат CapitalizedWords (a.k.a. Capitalized camelCase).
Значення змінної отримуйте з input(). Значення змінної складається з будь-якої кількості слів."""

a = input('Введить змінну у форматі snake_case: ')
b = a.split('_')
c = map(str.capitalize, b)
capitalized = ''.join(c)
print(capitalized)
