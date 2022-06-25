#10c_g.py
#숫자 추측해 맞히기
#understand what needs to be included 

import random

n = random. randint(1,100)
print(f'정답: {n}')
c = 0
msg = ''

while True:
    u = int(input('맞혀 보세요: '))
    c = c+1

    if abs(u-n) >= 20:
        msg = '*2'
    else:
        msg = ''

        
    if u == n:
        print('정답!')
        break
    elif u < n:
        print(f'UP{msg}')
    else:
        print('DOWN{msg}')

print(f'시도횟수: {c}번')
        
