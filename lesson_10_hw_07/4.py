"""Завдання 4.
Для зручності проведення вступних іспитів, усіх абітуріентів MIT розбивають на групи з залежності від перших літер
їхніх прізвищ. Групи називаються "A-I", "J-P", "Q-T", "U-Z". Назва групи визначає, в яку групу потрапляє абітуріентка,
в залежності від першої літери її прізвища. Наприклад, Will Smith потрапить в групу "Q-T", т.я.
перша літера його прізвища потрапляє в діапазон букв 'Q' та 'T' включно. Абітуріент Jay Z потрапить в групу "U-Z".
Написати функцію, що приймає параметром список імен студентів виду ['Name1 Surname1', 'Name2 Surname2',
'Name3 Surname3', ...] і повертає кількість абітуріентів в групах, сформованим за прізвищами описаним вище чином.
def group_by_surname(list_of_enrollees): # returns 4 ints
    pass"""


def group_by_surname(list_of_enrollees):
    groups = {'A-I': 0, 'J-P': 0, 'Q-T': 0, 'U-Z': 0}
    for student in list_of_enrollees:
        first_letter = student.split()[1][0]
        if 'A' <= first_letter <= 'I':
            groups['A-I'] += 1
        elif 'J' <= first_letter <= 'P':
            groups['J-P'] += 1
        elif 'Q' <= first_letter <= 'T':
            groups['Q-T'] += 1
        elif 'U' <= first_letter <= 'Z':
            groups['U-Z'] += 1
    return list(groups.values())


student_lst = ['Mark One', 'Tom Two', 'Mary Five', 'Will Smith', 'Jay Zee']
print(group_by_surname(student_lst))
