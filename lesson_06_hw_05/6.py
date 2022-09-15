""" Завдання 6.
Написати функцію, що розраховує суму Unicode кодів усіх символів,
що знаходяться між двома заданими символами включно. Наприклад, в функцію передаються символи 'a' та 'd',
отже треба порахувати суму кодів символів 'a', 'b', 'c' та 'd', а це 97+98+99+100=394.
"""


def sum_symbol_codes(first, last):
    first_ord = ord(first)
    last_ord = ord(last)
    sum_num = 0
    for i in range(first_ord, last_ord + 1):
        sum_num += i
    return sum_num


def main():
    symbol_first = input('Введить перший символ: ')
    symbol_last = input('Введить другий символ: ')
    print('Сума кодів цих символів дорівнює:', sum_symbol_codes(symbol_first, symbol_last))


main()
