#15d_1.py
#숫자목록 추출

import random

n = list(range(1,10)) #1~9 숫자목록 

# 무작위 5개 수 출력하기(원본이 바뀌지 않)
print('1~9 무작위 추출')
for x in range(5):
    one = random.choice(n)
    print(one)

print(f' 숫자 목록: {n}')


#중복없이 무작위 5개 수 출력
print('1~9 무작위 추출')
random.shuffle(n)
for x in range(5):
    print(n[x])
print(f'숫자 목록: {n}')
