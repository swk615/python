#09c_c.py
#덧셈 문제 맞추기
#반복되어야 하는 부분 위에다가 for x in range (all scroll &tab)
#x는 0에서 시작
# ==
#s1 = 0, s1=s1+1

import random
import time

s1 = 0
s2 = 0

start = time.time()

for x in range(10):
    n1 = random. randint(1,10)
    n2 = random. randint(1,10)

    usr= int(input(f'{x+1}. {n1}+{n2} = '))
    if usr == n1+n2:
        print('정답!')
        s1 = s1 + 1
    else:
        print('오답!')
        s2 = s2 + 1

end = time.time()
et = int(end - start)

print('-' *30)
print(f'시간: {et}초')
print(f'정답: {s1}개')
print(f'오답: {s2}개')

if s1 == 10 and et< 30:
    print('당신은 덧셈의 신!')

#모두 정답이면 '당신은 덧셈의 신!' 출력하기 
