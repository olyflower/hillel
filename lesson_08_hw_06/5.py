"""Завдання 5.
Написати функцію, що повертає усі прості числа від 1 до 100 у вигляді списку."""


def gen_primes():
    result = [2, 3, 5, 7]
    for i in range(2, 101):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            result.append(i)
    return result


print('Всі прості числа від 1 до 100', gen_primes())
