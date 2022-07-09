

def tra(b,u,h):
    a = (b+u)*h/2
    return a

print('사다리꼴 면적을 구하는 프로그램')
print()
u = int(input('윗변의 길이를 입력하세요: '))
b = int(input('밑변의 길이를 입력하세요: '))
h = int(input('높이의 길이를 입력하세요: '))

a = tra(b,u,h)
print()
print(f'면적은 {a}입니다')
