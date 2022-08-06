#trun_01.py
#터틀런

import turtle as t
import random 

#화면설정
t.setup(500,500)
t.bgcolor('orange')

def t_setup(t_name, x,y,c = 'white',s = 'turtle'):
    t_name.shape(s)
    t_name.color(c)
    t_name.up()
    t_name.speed(0)
    t_name.goto(x,y)

def t_up():
    t.setheading(90)
def t_down():
    t.setheading(270)
def t_left():
    t.setheading(180)
def t_right():
    t.setheading(0)
def ts_move():
    ts_x = random.randint(-230, 230)
    ts_y = random.randint(-230,230)
    ts.goto(ts_x, ts_y)
    
def t_check():
    if  t.xcor()>225:
        t.setx(225)
    elif t.xcor()<-230:
        t.setx(-230)
    if t.ycor()>225:    #x,y와 관련이 없으니 if 두개로 
        t.sety(225)
    elif t.ycor()<-225:
        t.sety(-225)
def te_move():
    te_ang = te.towards(t.pos())
    te.setheading(te_ang)
    te.forward(4)

def play():
    t.forward(10)
    #플레이어 좌표확인(t_check())
        
    #if  t.xcor()>225:
        #t.setx(225)
    #elif t.xcor()<-230:
        #t.setx(-230)
    #if t.ycor()>225:    #x,y와 관련이 없으니 if 두개로 
        #t.sety(225)
    #elif t.ycor()<-225:
        #t.sety(-225)

    #먹이충돌
    d = t.distance(ts)
    #print(f' 먹이와 거북이 거리: {d}')
    if d<12:
        ts_move()
        #먹이를 다른 장소로 이동 (ts-move())
        
        #ts_x = random.randint(-230, 230)
        #ts_y = random.randint(-230,230)
        #ts.goto(ts_x, ts_y)

    #악당 거북이 이동(te_move())
    #te_ang = te.towards(t.pos())
    #te.setheading(te_ang)
    #te.forward(4)
    te_move()
    

    #악당충돌 확인
    #1.악당과의 거리 측정(d_te)
    #2.악당과 거리가 12이상이면 타이머 실행
    
    d_te = t.distance(te)
    if d_te>= 20:
        t.ontimer(play,100)  #1000ms = 1s
    
    
#ts 먹이
ts = t.Turtle()
t_setup(ts, 0, -200, 'green', 'circle')
#ts.shape('circle')
#ts.color('green')
#ts.speed(0)
#ts.up()
#ts.goto(0,-200)

#te 악당
te = t.Turtle()
t_setup(te, 0, 200, 'red')
#te.shape('turtle')
#te.color('red')
#te.speed(0)
#te.up()
#te.goto(0,200)

#t 플레이어
t_setup(t, 0, 0)
#t.shape('turtle')
#t.color('white')
#t.speed(0)
#t.up()


#키입력
t.onkeypress(t_up, 'Up')
t.onkeypress(t_down, 'Down')
t.onkeypress(t_left, 'Left')
t.onkeypress(t_right, 'Right')
t.listen()

#게임시작
play()
