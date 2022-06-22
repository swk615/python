#for3.py

import turtle as t

d=100
n=100

t.speed(0)
t.color('green')
t.bgcolor('gold')

for x in range(n):
    t.circle(d)
    t.left(360/n)
