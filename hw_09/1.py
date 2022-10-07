"""1. Написати функцію, яка отримує у вигляді параметра ім'я файлу назви інтернет доменів
 (domains.txt - https://gist.github.com/hodunov/6e43ab1637db677b34516603c4de30c2)
і повертає їх у вигляді списку рядків (назви повертати без крапки)."""


def get_domains(path):
    with open(path, 'r') as file:
        return list(map(lambda x: x[1:], file.read().split('\n')))


print(get_domains('domains.txt'))
