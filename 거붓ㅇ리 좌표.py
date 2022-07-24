#거북이 좌표 

원소값 변경가능 []
변경불가 ()

>>> import turtle as t
>>> 
>>> t.shape('turtle')
>>> 
>>> t.goto(100,100)
>>> t.pos()
(100.00,100.00)
>>> t.pos()[0]
100
>>> t.pos()[1]
100
>>> t.setheading(100)
>>> t.forward(50)
>>> t.xcor()
91.31759111665349
>>> t.ycor()
149.2403876506104
>>> t.pos()
(91.32,149.24)
>>> t.heading()
100.0
>>> t.write('turtle')

t.shape('turtle')
>>> t.write('Hello', False, "center", ("D2Coding", 30))
>>> t.goto(0,100)
>>> t.write('Hello', True, 'left', ('', 30))
