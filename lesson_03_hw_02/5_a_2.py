"""Завдання 5_а_2.
Написати програму, що вираховує суму усіх цифр трьохзначного числа введеного користувачем
через input(). Виконати програму в двох варіантах:
a) З використанням рядків"""

number = str(abs(int(input('Введить тризначне число: '))))
sum_number = int(list(number)[0]) + int(list(number)[1]) + int(list(number)[2])
print('Сума цифр числа', number, 'дорівнює', sum_number)
