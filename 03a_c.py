# 03a_c.py
#연산자

x = 5
y = 3

print(x, '+', y, '=', x+y)
print(f'{x}-{y}={x-y}')

n = input('몇번을 반복할까요?')
n=int(n)
for x in range(n):
    print(f'{x+1}python!')
print('end for')


