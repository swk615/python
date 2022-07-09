#도형그리기 함수 step 1

import turtle as t 


#한변의 길이가 npx인 사각형을 그리는 함수

def draw_rect(n):
    for x in range(4):
        t.forward(n)
        t.left(90)

#한변의 길이가 npx인 삼각형을 그리는 함수
        
def draw_tri(n):
    for x in range(3):
        t.forward(n)
        t.left(120)


#실행 
draw_rect(100)
draw_rect(50)
draw_tri(90)
draw_tri(30)
