"""Завдання 6.
За реузлтьаатми длосдіжнеь ооднго аглнісйкього уінвсрееитут, не має зчнаннея, в якмоу пояркду рзтооашвнаі
лтіери у совлі. Гоолвен, щоб пшреа та оастння ліетри блуи на сєвому мсіці. Ретша летір мжоуть сділаувти
в абосюлтно впиакдомову поярдук, все ондо ткест чатиитмтьеся без пброемл. Прчиниою цгоьо є те,
що ми чтаимєо не кножу бкуву окером, а усе совло раозм.
Напишіть функцію, яка прийматиме рядок та перетворюватиме його способом, описаним вище. В якості алгоритму
перемішування букв використовуйте наступні кроки для кожного слова в тексті:

Залишаєте на місці перший та останні символи слова
З тих, що лишилися, беремо перші три символа та перемішуємо в довільному порядку
Отриману перемішану трійку додаємо до результату
Повторюємо з пункту 2 допоки не закінчаться неперемішані символи
def pemrtuate(text):  # returns permuted text
    pass"""

import random


def pemrtuate(text):
    text = text.split()
    text_res = ''

    for idx, word in enumerate(text):
        i = 1
        n = 3
        word_new = word[0]

        while n > 1:
            n = 3 if len(word) - i - 1 > 3 else len(word) - i - 1
            slice = list(word[i:i+n])
            while slice == list(word[i:i+n]) and n > 1:
                random.shuffle(slice)
            word_new += ''.join(slice)
            i += n
        if len(word) > 1:
            word_new += word[-1]
        if idx == len(text) - 1:
            text_res += word_new
        else:
            text_res += word_new + ' '
    return text_res


my_list = 'За результатами досліджень одного англійського університету, не має значення,' \
              ' в якому порядку розташовані літери у слові.'

print(pemrtuate(my_list))
