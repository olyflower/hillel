"""Завдання 2.
Створити два класи: Круг і Точка (на площині -- є дві осі координат). Створити в класі Круг метод, що, в якості
параметра, приймає екземпляр Точки, перевіряє, чи дана точка знаходиться всередині круга, і повертає,
відповідне булеве значення."""


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def is_in_circle(self, point):
        return (point.x - self.x) ** 2 + (point.y - self.y) ** 2 <= self.r ** 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


circle = Circle(12, 20, 50)
point_one = Point(-5, 0)
print(circle.is_in_circle(point_one))
