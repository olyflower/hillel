"""2. Написати функцію, яка отримує у вигляді параметра ім'я файлу (
names.txt - https://gist.github.com/hodunov/53c318071591df382bb08b11029b8e11)
і повертає список усіх прізвищ із нього.
Кожен рядок файлу містить номер, прізвище, країну, деяке число (таблиця взята з вікіпедії).
Роздільник - символ табуляції "\t"""


def get_names(path):
    with open(path, 'r') as file:
        return list(map(lambda x: x.split('\t')[1], file.read().split('\n')))


print(get_names('names.txt'))
