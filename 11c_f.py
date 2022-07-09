#11c_f.py
# 반환값이 있는 함수

#함수이름결정, 인수(멤버변수)사용결정, 반환값 결정
#1.def 함수이름(), 2.def 함수이름(인수), 3.def 함수이름(인수)
                                              #return 반환값

#제곱을 구하는 함수 square(num)
def square(num):
    res = num * num  #res = num **2
    return res

#삼각형 넓이 구하는 함수 tri(b 밑변,h 높이)
def tri(b,h):
    a = b*h / 2
    return a

#4의 제곱 구하기
r = square(4)
print(r)

r = square(4) + square(5)
print(r)

r = tri(3,10)
print(r2)
