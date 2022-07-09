#12b_f.py
#1~n 곱 구하는 함수 fact(n)
#n+1 하는 이유 = n-1까지 나열하기 때문 

def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f

#1~4곱 구하기
print(fact(10))
