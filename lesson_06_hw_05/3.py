""" Завдання 3.
Написати функцію, що знаходить різницю між сумою усіх парних чисел та сумою усіх непарних чисел
серед num_limit випадкових чисел згенерованих в заданому діапазоні lower_bound..upper_bound.
Для генерації чисел використайте модуль random (можна використати будь-яку зі зручних для вас функцій модулю,
наприклад randint).
"""

from random import randint


def diff_odd_even(num_limit, lower_bound, upper_bound):
    list_num = []
    sum_even = 0
    sum_odd = 0
    for i in range(num_limit):
        list_num.append(randint(lower_bound, upper_bound))
        if list_num[i] % 2 == 0:
            sum_even += list_num[i]
        else:
            sum_odd += list_num[i]
    # print(list_num)
    return sum_even - sum_odd


def main():
    num_limit_1 = int(input('Введить кількість цифр: '))
    lower_bound_1 = int(input('Введить нижню межу цифр: '))
    upper_bound_1 = int(input('Введить верхню межу цифр: '))
    print('Різниця між сумою усіх парних чисел та сумою усіх непарних чисел:', diff_odd_even(num_limit_1, lower_bound_1, upper_bound_1))


main()
