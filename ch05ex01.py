#ch05ex01.py
#태극기모양 그리기

import turtle as t


t.bgcolor('black')
t.speed(0)
for x in range(500):
    t.forward(x)
    t.left(89)

    if x%4 == 0:
        col = 'red'
    elif x%4 == 1:
        col = 'yellow'
    elif x%4 == 2:
        col = 'blue'
    else:
        col = 'green'


    t.color(col)
    
