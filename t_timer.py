#t_timer.py
#0.1초마다 이동하는 거북이 

def t_move():
    t.forward(10)
    if t.xcor()>250:
        t.goto(-250,0)

    t.ontimer(t_move,100)

#화면설정
import turtle as t
t.bgcolor('orange')
t.setup(500,500)



#거북이 설정 
t.shape('turtle')
t.color('white')
t.up()
t.goto(-250,0)
t.speed(0) #없으면 다시 처음으로 돌아가는게 보임 

#거북이 이동 
t_move()
