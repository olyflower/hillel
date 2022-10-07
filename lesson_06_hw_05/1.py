""" Завдання 1.
Створити програму, що виводить на екран числа від 1 до 100 при цьому заміняючи:
числа, що діляться на 3, на рядок Fizz
числа, що діляться на 5, на рядок Buzz
числа, що діляться і на 3, і на 5, на рядок FizzBuzz"""

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        number = 'FizzBuzz'
    elif number % 3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'
    print(number)
