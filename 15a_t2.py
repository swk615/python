#15a_t2.py
#타자게임 만들기

import random
import time 

#단어리스트
w = ['cat', 'dog', 'fox', 'monkey', 'mouse',
     'panda', 'frog', 'snake', 'wolf']

#게임 시작 안내
input('[타자게임] 준비되면 엔터!')
start = time.time() #시작시간 

#문제 초기화(변수:n,q)
q = random.choice(w)
n = 1
#게임루프
while n<6:
    print(f'문제 {n}')
    print(q)
   #문제출제
   #사용자 입력(변수:u)
    u = input()
   #정타, 오타 확인
   #정타시 '통과!', 오타시 '오타! 다시도전!'
    if u == q:
        print('통과!')
        n = n+1
        q = random.choice(w)
    else:
        print('오타! 다시 도전!')

#타자 모두 입력시 종료시간 측정 
end = time.time()  #끝나는 시간
et = end - start

print(f'타자시간: {et:.1f}초')  #.1f 소수점 첫째자리까지 
