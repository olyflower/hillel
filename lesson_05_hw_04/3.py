# Завдання 3.
# Написати функцію, що відповідає на питання, чи перетинають два заданих кола на площині.
# Кожне коло задається координатами центра та радіусом.

# def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value

def circles_intersect(x1, y1, r1, x2, y2, r2):
    r = r1 + r2
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    if r >= d > abs(r1 - r2):
        return True
    else:
        return False


r1 = float(input('Введить радіус першого кола: '))
r2 = float(input('Введить радіус другого кола: '))
x1 = float(input('Введить координату x центра першого кола: '))
y1 = float(input('Введить координату y центра першого кола: '))
x2 = float(input('Введить координату x центра першого кола: '))
y2 = float(input('Введить координату y центра першого кола: '))

res = circles_intersect(x1, y1, r1, x2, y2, r2)

if res:
    print('Задані кола перетинаються')
else:
    print('Задані кола не перетинаються')
