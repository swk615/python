#15a_t4.py
#타자게임 만들기

import random
import time

#단어리스트
w = ['고양이', '강아지', '여우',
     '원숭이', '쥐', '판다', '개구리',
     '뱀', '늑대']

#단어 원소 재배치
random.shuffle(w)

#문제번호 초기화
n = 1

#게임시작 안내
print('게임을 시작하려면 엔터!')
input()

start = time.time()

#게임 루프
while n < 6:
    #문제출제 및 입력
    print(f'*문제{n}')
    print(w[n])   #셔플을 해둔 후 나오는 문제를 나타냄 
    u = input()

    # 정타확인
    if u == n:
        print('통과')
    else:
        print('오타! 다시 입력!')
        
#게임 종료 시작 측정
end = time.time()
et = end - start
print(f'타자시간: {et:.1f}초')
