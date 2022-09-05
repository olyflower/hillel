# Завдання 4.
# Напишіть програму, яка зчитує ціле число та виводить текст, аналогічний наведеному у прикладі
# (пробіли та переведення на новий рядок важливі!).
# Перший рядок містить наступне значення, а другий рядок містить попереднє значення введеного числа:

number = int(input('Please enter an integer number: '))
number_next = number + 1
number_previous = number - 1

print('Next number for number', number, 'is', number_next)
print('Previous number for number', number, 'is', number_previous)


