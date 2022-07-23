#15b_1.py
#태극모양 그리기

import turtle as t

t.bgcolor('black')
t.speed(0)

col = ['red', 'blue', 'green']
for x in range(500):
    #if x%3 == 0:
        #t.color('red')
    #elif x%3 == 1:
        #t.color('yellow')
   # else:
        #t.color('blue')

    t.forward(x)
    t.left(119)
    t.color(col[x%3])
