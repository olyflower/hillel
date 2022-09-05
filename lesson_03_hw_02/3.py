# Завдання 3.
# Написати програму, що перетворює значення рядкової змінної з формату snake_case в формат
# CapitalizedWords (a.k.a. Capitalized camelCase). Значення змінної отримуйте з input().
# Для простоти вважаємо, що значення змінної завжди складається з 3-х слів.
# Наприклад: 'employee_first_name' -> 'EmployeeFirstName'.

a = input('Введить змінну у форматі snake_case (3 слова): ')
c = a.title()
b = c.split('_')
result = b[0] + b[1] + b[2]
print(result)
