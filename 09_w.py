#09a_w.ppy
#마음대로 걷는 거북이

import turtle as t
import random

t.shape('turtle')
t.speed(0)

for x in range(500):
    ang = random. randint(1,360)
    d = random. randint(1,20)
    t.setheading(ang)
    t.forward(d)
