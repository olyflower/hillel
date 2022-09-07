# Завдання 5.
# У математиці функцію `sign(x)` (знак числа) визначено так:
#   sign(x) = 1, якщо x > 0,
#   sign(x) = -1, якщо x < 0,
#   sign(x) = 0, якщо x = 0.
# Для введеного користувачем числа x виведіть значення sign(x).
# Це завдання бажано вирішити за допомогою каскадних інструкцій if... elif... else.


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


number = float(input('Введить число: '))
print(sign(number))
