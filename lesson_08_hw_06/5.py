"""Завдання 5.
Написати функцію, що повертає усі прості числа від 1 до 100 у вигляді списку."""


def gen_primes(n):
    result = [2, 3, 5, 7]
    for i in range(2, n + 1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            result.append(i)
    return result


number = int(input('Введить число,до якого виводити всі прості числа: '))
print('Всі прості числа від 1 до', number, ':', gen_primes(number))
