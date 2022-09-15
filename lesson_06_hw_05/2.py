""" Завдання 2.
Написати функцію, що знаходить різницю між максимальним та мінімальним значенням
з num_limit випадкових чисел згенерованих в заданому діапазоні lower_bound..upper_bound.
Для генерації чисел використайте модуль random (можна використати будь-яку зі зручних для вас функцій модулю,
наприклад randint).
"""

from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound):
    if num_limit == 0:
        return None
    list_num = []
    for i in range(num_limit):
        list_num.append(randint(lower_bound, upper_bound))
    max_num = max(list_num)
    min_num = min(list_num)
    # print(list_num)
    return max_num - min_num


def main():
    num_limit_1 = int(input('Введить кількість цифр: '))
    lower_bound_1 = int(input('Введить нижню межу цифр: '))
    upper_bound_1 = int(input('Введить верхню межу цифр: '))
    result = diff_min_max(num_limit_1, lower_bound_1, upper_bound_1)
    if result is not None:
        print('Різниця між максимальним та мінімальним значенням:', result)
    else:
        print('Список порожній')


main()
