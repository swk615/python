#18_tl.py
#터틀런

import turtle as t
import random

#변수초기화
score = 0
playing = False

def set_turtle(tname, tshape, tcol, tx, ty):
    tname.shape(tshape)    #'' ㄴ
    tname.color(tcol)
    tname.speed(0)
    tname.up()
    tname.goto(tx, ty)


def turn_up():
    t.setheading(90)
def turn_down():
    t.setheading(270)
def turn_left():
    t.setheading(180)
def turn_right():
    t.setheading(0)
def speed_up():
    t.forward(10)
    
def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

#시작 화면 구현
def message(m1,m2):
    t.goto(0,100)
    t.write(m1, False , 'center', ('D2Coding', 35))#False = 거북이 이동여부
    t.goto(0,-100)
    t.write(m2, False, 'center', ('D2Coding', 15))
    t.home()  #turtle 0,0으로 보내기 


#화면초기화
def reset_game():
    global score
    score = 0
    set_turtle(ts, 'circle', 'green', 0, -200)
    set_turtle(te, 'turtle', 'red', 0,200)
    set_turtle(t, 'turtle', 'white', 0,0)
    te.setheading(0)
    ts.setheading(0)

def check_ts():
    global score
    d = t.distance(ts)
    if d < 12: #충돌허용범위
        score = score+1
        ts.write(score)
        ts_x = random.randint(-230, 230)
        ts_y = random.randint(-230, 230)
        ts.goto(ts_x, ts_y)

def move_te():
    global score
    r = random.randint(1,5)
    if r == 2:
        ang = te.towards(t.pos())
        te.setheading(ang)
    te_s = score +5
    if te_s > 12:
        te_s = 12
    te.forward(te_s)
def check_te():
    global playing   #죽고 난 후 거북이의 상태 
    d = t.distance(te)
    if d < 12:
        playing = False
        message('GAME OVER', f'SCORE: {score}')
        reset_game()


def play():
    #글로벌 변수 설정
    global score, playing
    t.forward(10)

    #먹이의 충돌
    check_ts()

    #악당 이동, 충돌
    move_te()
    check_te()

   #게임진행 판단
    if playing:
        t.ontimer(play,100)  #0.1초 후에 play 함수 실행 

    
#배경화면 설정
t.setup(500,500)
t.bgcolor('orange')

#악당거북이 생성
te = t.Turtle()
#set_turtle(te, 'turtle', 'red', 0,200)   #''
#te.shape('turtle')
#te.color('red')
#te.speed(0)
#te.up()
#te.goto(0,200)

#먹이 생성
ts = t.Turtle()
#set_turtle(ts, 'circle', 'green', 0, -200)
#ts.shape('circle')
#ts.color('green')
#ts.speed(0)
#ts.up()
#ts.goto(0,-200)

#게임 초기화
reset_game()
#시작화면구현
#message(m1,m2) 함수구현 
message('Turtle RUN', 'SPACE')

#플레이어
#set_turtle(t, 'turtle', 'white', 0,0)
#t.shape('turtle')
#t.color('white')
#t.speed(0)
#t.up()

#키입력
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_right, 'Right')
t.onkeypress(start, 'space')
t.onkeypress(speed_up, 's')
t.listen()

#게임진행

