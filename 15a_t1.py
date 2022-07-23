#15a_t1.py
#문제목록 만들기

import random

#단어 리스트
w = ['cat', 'dog', 'fox', 'monkey',
     'mouse', 'panda', 'frog', 'snake', 'wolf']

#문제번호 n
n = 0

for x in range(5):
    q = random.choice(w)
    print(f'{n+1}. {q}')
    #n = n+1
