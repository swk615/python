#ch06ex02.py

import random

def make_quiz():
    n1 = random.randint(10,20)
    n2 = random.randint(1,10)
    q = f'{n1} - {n2}'
    return q


for x in range(5):
    q = make_quiz()
    a = eval(q)
    print(f'{q} = {a}')
