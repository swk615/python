#16a_c2.py
#타겟그리기

#대포는 항상 마지막
#1.바닥 2.타겟 3.대포

import turtle as t
import random

#변수 초기화
l = 200

#바닥그리기
t.goto(300,0)
t.goto(-300,0)

#타겟그리기
tx = random.randint(50,150)

t.color('green')
t.pensize(5)

t.up()
t.goto(tx- l/2,3)
t.down()
t.goto(tx+l/2,3)   #50를 만들기 위해
print(f'타겟좌표: {tx}, 길이: {l}px')

#대포초기화
t.up()
t.color('black')
t.goto(-200,10)
t.setheading(20)
