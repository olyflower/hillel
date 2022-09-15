""" Завдання 4_a.
Написати функцію, що повертає найбільшу цифру випадково згенерованого 12-ти-значного натурального числа.
# б) без використання рядків.
"""

from random import randint


def get_max_digit(number):
    max_number = 0
    while number > 0:
        last_number = number % 10
        if last_number > max_number:
            max_number = last_number
        number = number // 10
    return max_number


def main():
    number_12 = randint(100000000000, 999999999999)
    print('Випадково згенероване 12-ти значне натуральне число:', number_12)
    print('Найбільша цифра цього числа:', get_max_digit(number_12))


main()
