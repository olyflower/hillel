""" Завдання 4_a.
Написати функцію, що повертає найбільшу цифру випадково згенерованого 12-ти-значного натурального числа.
а) з використанням рядків.
"""

from random import randint


def get_max_digit(number):
    max_number = max(list(str(number)))
    return max_number


def main():
    number_12 = randint(100000000000, 999999999999)
    print('Випадково згенероване 12-ти значне натуральне число:', number_12)
    print('Найбільша цифра цього числа:', get_max_digit(number_12))


main()
