#15c_2.py
#n = list(range(1,10)) >>> n
#[1, 2, 3, 4, 5, 6, 7, 8, 9]

import random

def make_quiz():
    n1 = random.randint(10,20)
    n2 = random.randint(10,20)
    op = random.randint(0,3)
    ops = ['+', '-', '*', '/']
    q = f'{n1}{ops[op]}{n2}'
    return q

for x in range(10):
    q = make_quiz()
    a = eval(q)
    print(f'{q} = {a}')
