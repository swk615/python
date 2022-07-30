# timer1.py
#1초후에 인사하기

import turtle as t

def hello():
    print('Hello~')
    t.ontimer(hello,1000)

def t_move():
    t.forward(10)
    print(f'x: {t.xcor()}')
    if t.xcor()<290:
        t.ontimer(t_move,100)

#창설정
t.setup(700,300)
t.bgcolor('black')

#거북이 설정
t.shape('turtle')
t.color('yellow')
t.up()
t.goto(-300,0)

#거북이 이동
t_move()

