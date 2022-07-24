#16a_c3.py
#대포조절

import turtle as t
t.shape('turtle')
import random

#변수 초기화
l = 50
def reset_cannon(t_ang):
    t.color('black')
    t.goto(-200,10)
    t.setheading(t_ang)
    
def turn_up():
    t.left(2)


def turn_down():
    t.right(2)

def fire():
    ang = t. heading()
    while t.ycor()>0:
        t.forward(15)
        t.right(5)
        print(f'x: {t.xcor()}, y: {t.ycor()}')

        #타겟충돌확인
    d = t.distance(tx,0)
    if d <= l/2:
        t.color('blue')
        t.write('Good!', False, 'center', ('D2Coding', 15))
    else:
        t.color('red')
        t.write('Bad!', False, 'center', ('D2Coding', 15))
        reset_cannon(ang)
        #t.color('black')
        #t.goto(-200,10)
        #t.setheading(20)
    
#바닥그리기
t.goto(300,0)
t.goto(-300,0)

#타겟그리기
tx = random.randint(50,150)
t.pensize(5)
t.color('green')
t.up()
t.goto(tx-l/2, 3)
t.down()
t.goto(tx+l/2, 3)


#대포 초기화
t.up()
reset_cannon(20)
#t.color('black')
#t.goto(-200,10)
#t.setheading(20)

#키입력 처리
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, 'space')
t.listen()
