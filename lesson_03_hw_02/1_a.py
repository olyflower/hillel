"""Завдання 1_а.
Поміняти місцями значення змінних a та b для наступних випадків:
a) За допомогою третьої проміжної змінної c. Типи значень змінних можуть бути будь-якими.
Не можна використовувати списків, рядків, інших колекцій. В файлі має бути не більше трьох змінних a, b та c."""

a = input('Введить змінну а: ')
b = input('Введить змінну b: ')
c = a
a = b
b = c
print('Змінна а після заміни:', a)
print('Змінна b після заміни:', b)
