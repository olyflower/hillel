# Завдання 5_b
# Написати програму, що вираховує суму усіх цифр трьохзначного числа введеного користувачем
# через input(). Виконати програму в двох варіантах:
# b) Без використання рядків (після input() одразу приведіть текст до int()
# та не переводьте в рядок назад, а працюйте з цим числом)

number = abs(int(input('Введить тризначне число: ')))
sum_number = (number//100) + (number//10%10) + (number%10)
print('Сума цифр числа', number, 'дорівнює', sum_number)
