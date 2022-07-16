#14a_c.py
#계산문제 게임1
#q = str(n) + op >>> q '5-'

import random

def make_quiz():
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    op = random.randint(1,3)

    q = str(n1)
    if op == 1:
        q = q + '+'
    elif op == 2:
        q = q + '-'
    else:
        q = q + '*'
    q = q + str(n2)
    return q

q = make_quiz()
print(q)
