

import turtle as t

def move_t(x,y):
    t.up()
    t.goto(x,y)
    t.down()

def draw_poly(n,d,x,y):
    move_t(x,y) #이거 기억 
    for x in range(n):
        t.forward(d)
        t.left(360/n)
        

#실행 
draw_poly(5,50,150,150)
draw_poly(6,70,150,-150)
draw_poly(7,90,-150,-150)
draw_poly(8,110,-150,150)
