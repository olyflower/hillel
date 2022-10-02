"""Завдання 4.
Створити генератор паролів, що генерує паролі сумісні з наступними вимогами:
Пароль складається з 8 символів
В паролі допускаються лише великі та маленькі латинські літери, цифри та символ підкреслення "_"
Пароль обов'язково має містити щонайменше одну велику літеру, одну маленьку літеру та одну цифру
Не повинно бути більше 2 однакових символів підряд."""

import random


def gen_password():
    def letters_eq(lst):
        for i in range(len(lst) - 1):
            if lst[i] == lst[i+1]:
                return True

    list_password = '_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    password = ''.join(random.choice(list_password) for _ in range(8))
    while (not any(map(str.isdigit, password)) or
           not any(map(str.isupper, password)) or
           not any(map(str.islower, password)) or
           letters_eq(password)):
        password = ''.join(random.choice(list_password) for _ in range(8))
    return password


print(gen_password())
