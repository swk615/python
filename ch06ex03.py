#ch06ex03.py

import random

def make_quiz():
    n1 = random.randint(10,20)
    n2 = random.randint(10,20)
    op = random.randint(1,2)


    if op == 1:
        ops = '+'
    else:
        ops = '-'
        if n2>n1:
            n1,n2 = n2,n1

    q = f'{n1} {ops} {n2}'
    return q

for x in range(10):
    q = make_quiz()
    a = eval(q)
    print(f'{q} = {a}')
        

