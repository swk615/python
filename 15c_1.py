#15c_1.py
#문제함수 make_quiz()

import random

def make_quiz():
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    op = random.randint(1,3)
    
    
    #if op == 1:
        #ops = '+'
    #elif op == 2:
        #ops = '-'
   # else:
        #ops = '*'
   
    q = f'{n1}{ops}{n2}'
    return q

ops = ['+', '-', '*']

for x in range(10):
    q = make_quiz()
    print(q)
    q = f'{n1}{ops}{n2}'
    
    
