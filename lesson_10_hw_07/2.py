"""Завдання 2.
Написати функцію, що приймає безліч ітерабельних (не лише списків!) об'єктів, а повертає список з усіх елементі
цих об'єктів разом.
def lchain(*iterables):  # returns list
     pass
assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [1, 2, 3, '5', 6, 7, 8, 9]"""


def lchain(*iterables):
    lchain_list = []
    for elem in iterables:
        for i in elem:
            lchain_list.append(i)
    return lchain_list


print(lchain([1, 2, 3], {'5': 5}, (4, 5, 6), 'aaaa', range(8, 10)))
