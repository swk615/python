#10b_sum.py
#1~10  합 구하기
#ctrl c(break)

x = 1
s = 0

while x <= 10:
    s = s+x
    print(f'x: {x}, s: {s}')
    #x = x+1
    if s >1000:
        break
print(f'sum: {s}')
