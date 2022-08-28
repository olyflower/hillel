from decimal import *
a = Decimal(input('Введите сумму в гривне: '))
kurs = Decimal(39.90)
print('По состоянию на 26 августа 2022 года это составляет:', round(a/kurs, 2), 'долларов США')
