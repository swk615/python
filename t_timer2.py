#t_timer2.py

import turtle as t
import random 


#초기설정값
#t_speed = random.randint(8,20)
#ts_speed = random.randint(8,20)

def t_run():
    t_speed = random.randint(8,20)
    ts_speed = random.randint(8,20)
    t.forward(t_speed)
    ts.forward(ts_speed)
    if t.xcor()<300 and ts.xcor()<300:
        t.ontimer(t_run,100)

def d_line(se,sy,ex,ey):
    t.up()
    t.goto(se,sy)
    t.down()
    t.goto(ex,ey)
   
#창설정    
t.bgcolor('orange')
t.setup(700,300)

#트랙그리기
t.color('white')
t.speed(0)

d_line(-350,0,350,0)
d_line(-350,100,350,100)
d_line(-350,-100,350,-100)
#for ly in range(-100,101,100): d_line(-350,ly,350,ly)  range(시작값, 종료값+1, 증감값)

#흰거북이 
t.color('white')
t.shape('turtle')
t.up()
t.goto(-300,50)
t.speed(0)

#빨간 거북이 
ts = t.Turtle()
ts.color('red')
ts.shape('turtle')
ts.up()
ts.goto(-300,-50)
ts.speed(0)

#이동 
t_run()
