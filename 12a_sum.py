#12a_sum.py
#!~n 합 구하는 함수 sum_f(num)

def sum_f(num):
    s = 0
    for i in range(1,num+1):
        s = s + i
    return s

#1~5합구하기
r = sum_f(5)
print(r)

#1~10 합구하기
print(sum_f(10))

#1~100 합 구하기
print(sum_f(100))

