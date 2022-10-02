"""Завдання 5.
Написати функцію, що повертає усі прості числа від 1 до n у вигляді списку."""


def gen_primes(n):
    result = []
    for i in range(2, n + 1):
        k = 0
        for j in range(1, i + 1):
            if i % j == 0:
                k += 1
        if k == 2:
            result.append(i)
    return result


number = int(input('Введить число,до якого виводити всі прості числа: '))
print('Всі прості числа від 1 до', number, ':', gen_primes(number))
