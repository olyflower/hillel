""" Завдання 7.
Програма випадковим чином обирає число від 1 до 10 і пропонує користувачу його вгадати.
Користувач вводить число, а програма перевіряє його і, якщо користувач не вгадав,
що повідомляє ви введене число більше чи менше від згенерованого. Після цього знову просить вгадати.
І так, поки користувач не вгадає.
7_1. Число загадується в проміжку від 1 до 100
7_2. Після однієї гри, програма пропонує повторити.
"""

from random import randint

game = 'yes'
while game == 'yes':
    number = randint(1, 100)
    print(number)    # print загадане число для перевірки результату
    print('Гра вгадай число від 1 до 100!')
    number_user = 0

    while number_user != number:
        number_user = int(input('Введить число від 1 до 100: '))
        if number_user == number:
            print('Число вгадано вірно!', number)
            break
        if number_user < number:
            print('Введене число менше за загадане')
        elif number_user > number:
            print('Введене число більше за загадане')
    game = input('Грати ще раз? Якщо так, натисніть yes: ')
    if game != 'yes':
        print('Гра закінчена')