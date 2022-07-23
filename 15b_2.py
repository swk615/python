#15b_2.py
#태극모양 그리기(4색)
# 'red', 'yellow', 'blue', 'green'

import turtle as t

t.bgcolor('black')
t.speed(0)

col = ['red', 'yellow', 'blue', 'green']
for x in range(500):
    t.forward(x)
    t.left(89)
    t.color(col[x%4])
