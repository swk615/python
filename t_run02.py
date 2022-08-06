#t_run02.py
#터틀런
#te 악당, t player, ts 먹이 
import turtle as t
import random


def t_setup(t_name, t_x, t_y, t_col, t_shape):
    t_name.shape(t_shape)
    t_name.color(t_col)
    t_name.up()
    t_name.speed(0)
    t_name.goto(t_x, t_y)

    
def t_up():
    t.setheading(90)

    
def t_left():
    t.setheading(180)

    
def t_right():
    t.setheading(0)

    
def t_down():
    t.setheading(270)


def ts_move():
    ts_x = random.randint(-230, 230)
    ts_y = random.randint(-230,230)
    ts.goto(ts_x, ts_y)

    
def te_move():
    te_ang = te.towards(t.pos())
    te.setheading(te_ang)
    te.forward(4)

    
def t_check():
    #가로벽 확인
    if t.xcor()>225:
        t.setx(225)
    elif t.xcor()<-225:
        t.setx(-225)
    #세로벽 확인
    if t.ycor()>225:
        t.sety(225)
    elif t.ycor()<-225:
        t.sety(-225)


def play():
    #거북이 이동 및 벽충돌 확인 
    t.forward(10)
    t_check()
    #먹이 충돌
    d = t.distance(ts)
    if d<12:
        ts_move()
    #악당이동
    te_move()
    #악당충돌
    d_te = t.distance(te)
    if d_te>= 20:
        t.ontimer(play,100)
    


#배경화면 설정(플레이어, 악당, 먹이)
t.bgcolor('orange')
t.setup(500,500)
te = t.Turtle()
t_setup(te, 0, 200, 'red', 'turtle')
ts = t.Turtle()
t_setup(ts, 0, -200, 'green', 'circle')
t_setup(t, 0, 0, 'white', 'turtle')

#키 입력처리
t.onkeypress(t_up, 'Up')
t.onkeypress(t_left, 'Left')
t.onkeypress(t_right, 'Right')
t.onkeypress(t_down, 'Down')
t.listen()

#게임시작 함수 호출
play()
