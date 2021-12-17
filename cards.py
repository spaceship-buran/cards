print('Карты 0.1')
#Автор: Ермаков С.В.
#17/12/2022
from random import randint
import time
prt = int(input('Сколько партий? '))
n1 = input('Введите имя 1-ого играющего: ')
n2 = input('Введите имя 2-ого играющего: ')
score1 = 0
score2 = 0
for x in range(prt):
    print('Достаём карты...')
    time.sleep(3)
    carddst = randint(1, 13)
    cardmast = randint(1, 4)
    if carddst == 1:
        cdn = 'Двойка'
    elif carddst == 2:
        cdn = 'Тройка'
    elif carddst == 3:
        cdn = 'Четвёрка'
    elif carddst == 4:
        cdn = 'Пятёрка'
    elif carddst == 5:
        cdn = 'Шестёрка'
    elif carddst == 6:
        cdn = 'Семёрка'
    elif carddst == 7:
        cdn = 'Восьмёрка'
    elif carddst == 8:
        cdn = 'Девятка'
    elif carddst == 9:
        cdn = 'Десятка'
    elif carddst == 10:
        cdn = 'Валет'
    elif carddst == 11:
        cdn = 'Дама'
    elif carddst == 12:
        cdn = 'Король'
    else:
        cdn = 'Туз'
    if cardmast == 1:
        cmn = 'Бубнов'
    elif cardmast == 2:
        cmn = 'Червей'
    elif cardmast == 3:
        cmn = 'Пик'
    else:
        cmn = 'Треф'
    carddst1 = randint(1, 13)
    cardmast1 = randint(1, 4)
    if carddst1 == 1:
        cdn1 = 'Двойка'
    elif carddst1 == 2:
        cdn1 = 'Тройка'
    elif carddst1 == 3:
        cdn1 = 'Четвёрка'
    elif carddst1 == 4:
        cdn1 = 'Пятёрка'
    elif carddst1 == 5:
        cdn1 = 'Шестёрка'
    elif carddst1 == 6:
        cdn1 = 'Семёрка'
    elif carddst1 == 7:
        cdn = 'Восьмёрка'
    elif carddst1 == 8:
        cdn1 = 'Девятка'
    elif carddst1 == 9:
        cdn1 = 'Десятка'
    elif carddst1 == 10:
        cdn1 = 'Валет'
    elif carddst1 == 11:
        cdn1 = 'Дама'
    elif carddst1 == 12:
        cdn1 = 'Король'
    else:
        cdn1 = 'Туз'
    if cardmast1 == 1:
        cmn1 = 'Бубнов'
    elif cardmast1 == 2:
        cmn1 = 'Червей'
    elif cardmast1 == 3:
        cmn1 = 'Пик'
    else:
        cmn1 = 'Треф'
    cozir = randint(1, 4)
    if cozir == 1:
        ccn = 'Бубны'
    elif cozir == 2:
        ccn = 'Черви'
    elif cardmast1 == 3:
        ccn = 'Пики'
    else:
        ccn = 'Трефы'
    print('Стол: ')
    print('Козырь: ', ccn)
    print(n1, ':', '[', cdn, ']', '[', cmn, ']')
    print(n2, ':', '[', cdn1, ']', '[', cmn1, ']')
    time.sleep(5)
    if cardmast > cardmast1:
        if cardmast1 == cozir:
            print(n2, 'побил!')
            score2 += 1
        else:
            print(n1, 'побил!')
            score1 += 1
    elif cardmast < cardmast1:
        if cardmast == cozir:
            print(n1, 'побил!')
            score1 += 1
        else:
            print(n2, 'побил!')
            score2 += 1
    else:
        if carddst > carddst1:
            print(n1, 'побил!')
            score1 += 1
        elif carddst < carddst1:
            print(n2, 'побил!')
            score2 += 1
        else:
            print('Ничья!')
print('Итог: ')
time.sleep(3)
print(n1, ':', score1)
print(n2, ':', score2)
if score1 > score2:
    print(n1, 'выиграл!')
elif score1 < score2:
    print(n2, 'выиграл!')
else:
    print('Ничья!')
xt = input('Press "ENTER" to continue...')           
