#14a_c2.py
#계산문제
#eval(q)-->값 계산해 주는 함수
import random


def make_quiz():
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    op = random.randint(1,3)

    if op == 1:
            ops = '+'
    elif op == 2:
            ops = '-'
    else:
            ops = '*'
    q = f'{n1} {ops} {n2}'
    return q

#정답수 sc1
sc1 = 0
sc2 = 0
for x in range(5): 
    q = make_quiz()
    a = eval(q)
    #print(f'{q} = {a}')

    u = int(input(f'{q} = '))
    if u == a:
        print('정답!')
        sc1 = sc1+1
    else:
        print('오답!')
        sc2= sc2+1

    
print(f'정답: {sc1}개')
print(f'오답: {sc2}개')
if sc2 == 0:
    print('당신은 천재!!')
#오답이 없으면 '당신은 천제!!' 출력하기 
