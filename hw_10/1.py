"""Завдання 1.
Створити клас Годзіла. При створенні Годзіли вказується об'єм шлунку (параметром конструктора).
Для даного класу написати метод для поїдання людей eat. В даний метод параметром має передаватися об'єм людини
для поїдання; відповідно має зменшитися доступне місце в шлунку. Коли шлунок заповнюється більше,
ніж на 90%, то Годзіла, замість нормальної роботи методу має друкувати повідомлення, що він вже наївся і зараз
не може з'їсти більше людей."""


class Godzilla:
    def __init__(self, volume):
        self.volume = volume
        self.volume_current = 0

    def eat(self, human):
        if self.volume_current + human <= 0.9 * self.volume:
            self.volume_current += human
        else:
            print('I am full and do not want eat anymore!!!')


godzilla = Godzilla(50)
godzilla.eat(30)
godzilla.eat(16)
