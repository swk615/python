#ch18p2.py
#점수 올리기 함수 score()

#점수변수 초기화 
s = 0

def score():
    global s   #밖에 있는 s랑 같은 s이다 
    s = s+10
    print(s)



#점수 올리기
score()
score()
