#16a_cannon.py
#대포 게임 만들기

import turtle as t
import random

#변수초기화
l = 50

def draw_line(sx,sy,ex,ey,col = 'black', ps = 1):
    t.pensize(ps)
    t.color(col)
    t.up()
    t.goto(sx,sy)
    t.down()
    t.goto(ex, ey)
    
def reset_cannon(ang=20): #ang=20---> 값을 안정하면 20으로 간다 
    t.up()
    t.color('black')
    t.goto(-200,10)
    t.setheading(ang)
    
def turn_up():
    if t.heading()<90:
        t.left(2)
def turn_down():
    if t.heading()>0:
        t.right(2)

def prn_msg(txt,col='blue'):
    t.color(col)
    my = random.randint(10,150)
    t.sety(my)     #y좌표만 바꿔주는 것, setx 
    t.write(txt, False, 'center', ('D2Coding', 15))

def fire():
    ang = t.heading() #현재각도 알아내는 것 

    #바닥에 닿을때까지 이동하기 
    while t.ycor()>0:
        t.forward(15)
        t.right(5)

    #바닥에 닿으면 충돌확인하기
    d = t.distance(tx,0)
    if d <= l/2:
        prn_msg('Good!')
    else:
        prn_msg('Bad!', 'red')
        reset_cannon(ang)

#바닥그리기
draw_line(-300, 0, 300, 0)

#타겟그리기
tx = random.randint(50,150)
draw_line(tx-l/2, 3, tx+l/2, 3, 'green', 5)

#대포초기화
reset_cannon()
t.onkeypress(turn_up,'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(fire, 'space')
t.listen()
