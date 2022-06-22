#for1.py
#반복문

import turtle as t

d=100
n=5


#삼각형 그리기
for x in range(3):
    t.forward(d)
    t.left(120)
t.color('red')
t.pensize(10)
#사각형 그리기
for x in range(4):
    t.forward(d)
    t.left(90)
t.color('skyblue')
t.pensize(14)
#n각형 그리기
for x in range(n):
    t.forward(d)
    t.left(360/n)
t.color('green')
t.pensize(17)
#원그리기
t.circle(d//2)

