
import turtle as t

def move(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    
#x,y좌표에 한변의 길이 npx 사각형 그리기 
def draw_rect(x,y,n):
    #x,y로 이동
    move(x,y)
    #한변의 길이 n 사각형 그리기 
    for x in range(4):
        t.forward(n)
        t.left(90)
        
#x,y좌표에 한변의 길이 npx 삼각형 그리기 
def draw_tri(x,y,n):
    move(x,y)
    for x in range(3):
        t.forward(n)
        t.left(120)

#실행 
draw_rect(200,200,100)
draw_rect(-200,-200,100)
draw_tri(-200,200,100)
draw_tri(200,-200,100)

