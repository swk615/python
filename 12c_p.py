#12c_p.py
#다각형 그리기 함수 poly(n)
#pass = 이따가 다시 입력할게 

import turtle as t
t.shape('turtle')

#한변의 길이가 50인 다각형 그리기
def poly(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

#사각형 그리기
poly(4)

#오각형 그리기
poly(5)

#팔각형 그리기
poly(8)


#한변의 길이가 d인 n각형 그리기 함수 poly2(n,d)정의하기 
def poly2(n,d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)



#한변의 길이가 100px인 4각형 그리기
poly2(4,100)

#한변의 길이가 200px인 3각형 그리기 
poly2(3,200)

#한변의 길이가 70px인 8각형 그리기 
poly2(8,70)
