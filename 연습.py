#ch02ex02.py
#정수판별
num = int(input('정수를 입력하세요:'))

if num < 0:
    print('음수입니다')
elif num > 0:
    print('양수입니다')
else:
    print('0입니다')
