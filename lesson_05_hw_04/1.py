# Завдання 1.
# Написати функцію, що визначає чи введене число є парним.


def number_even_odd(number):
    if number % 2 == 0:
        print('Число є парним')
    else:
        print('Число є непарним')


a = int(input('Введить число: '))
number_even_odd(a)
