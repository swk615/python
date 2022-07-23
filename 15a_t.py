#15a_t.py
#타자게임만들기

import random

#단어리스트
w = ['cat', 'dog', 'fox', 'monkey', 'mouse',
     'panda', 'frog', 'snake', 'wolf']

n = 1
q = random.choice(w)
while n<6:
    print(f'*문제 {n}')
    print(q)
    #n = n+1
    #q = random.choice(w)
    
    u = input()

    
#정타시 문제번호 증가하고 문제 바꾸기('통과!'출력)
#오타시 '오타!다시 도전!' 출력하기
    
    if u == q:
        n = n+1
        q = random.choice(w)
        print('통과!')
    else:
        print('오타! 다시 도전!')
