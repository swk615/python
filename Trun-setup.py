#Trun-setup.py

import turtle as t
t.setup(500,500)
t.bgcolor('orange')

te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0,200)
te.down()

ts = t.Turtle()
ts.shape('circle')
ts.color('green')
ts.speed(0)
ts.up()
ts.goto(0,-200)
ts.down()

t.shape('turtle')
t.color('white')
t.speed(0)
t.up()


