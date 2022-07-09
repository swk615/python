#도형그리기 함수 step1


import turtle as t

#n을 넣는건 n각형을 그리기 위해서(정해져 있다면 n을 넣을 필요가 없다)

#사각형 그리기 함수
def draw_rect():
    for x in range(4):
        t.forward(50)
        t.left(90)

#삼각형 그리기 함수 
def draw_tri():
    for x in range(3):
        t.forward(50)
        t.left(120)

#코드 시작 
draw_rect()
draw_tri()
