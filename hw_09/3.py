"""Написати функцію, яка отримує у вигляді параметра ім'я файлу (
authors.txt - https://gist.github.com/hodunov/2d70c9611713b92d324ae7700d150a32) і повертає список
словників виду {"date_original": date_original, "date_modified": date_modified}
в яких date_original - це дата з рядка (якщо є),
а date_modified - ця ж дата, представлена у форматі "dd/mm/yyyyy" (d-день, m-місяць, y-рік)
Наприклад [{"date_original": "8th February 1828", "date_modified": 08/02/1828}, ...]."""

from dateutil.parser import parse


def get_authors(path):
    with open(path, 'r') as file:
        result_dict = []
        for line in file.read().split('\n'):
            if line.find(' - ') != -1:
                original = line[:line.find(' - ')]
                modified = parse(original).strftime('%m/%d/%Y')
                result_dict.append({'date_original': original, 'date_modified': modified})
        return result_dict


print(get_authors('authors.txt'))
