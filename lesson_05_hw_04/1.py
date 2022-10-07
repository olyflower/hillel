"""Завдання 1.
Написати функцію, що визначає чи введене число є парним."""


def is_even(number):
    return number % 2 == 0


a = int(input('Введить число: '))
if is_even(a):
    print('Парне число')
else:
    print('Непарне число')
