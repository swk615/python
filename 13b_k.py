#13b_k.py
#키보드 입력(명령 실행하기 위해서 함수 먼저 만들기)

import turtle as t
t.shape('turtle')
t.speed(0)

def t_up():
    t.setheading(90)
    t.forward(20)

def t_left():
    t.setheading(180)
    t.forward(20)

def t_right():
    t.setheading(0)
    t.forward(20)
def t_down():
    t.setheading(270)
    t.forward(20)

def clr_sc():
    t.clear() #화면만 지우기, t가 그자리에 계속 있음 
    t.reset() #화면을 지우고 원점으로 이동 
def p_up():
    t.penup()
def p_down():
    t.pendown()
def c_red():
    t.color('red')
def c_black():
    t.color('black')
def c_blue():
    t.color('blue')
def ps_1():
    t.pensize(1)
def ps_5():
    t.pensize(5)
def ps_10():
    t.pensize(10)
    
t.onkeypress(t_up, 'Up') #w 누르면 명령 실행해
t.onkeypress(t_left, 'Left')
t.onkeypress(t_right, 'Right')
t.onkeypress(t_down, 'Down')
t.onkeypress(clr_sc, 'Escape')
t.onkeypress(p_up, 'u')
t.onkeypress(p_down, 'd')
t.onkeypress(c_red, 'r')
t.onkeypress(c_black, 'k')
t.onkeypress(c_blue, 'b')
t.onkeypress(ps_1, '1')
t.onkeypress(ps_5, '2')
t.onkeypress(ps_10, '3')
t.listen() #대기상태
