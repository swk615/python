#ch01ex3
#화폐 교환기

pay = int(input('교환할 금액을 입력하세요: '))
print()

change = pay
print(f'교환금액: {pay}')

cnt = change // 50000
print(f'50000원: {cnt}')

change = change % 50000
cnt =change // 10000
print(f'10000원: {cnt}')

change = change%10000
cnt = change // 5000
print(f'5000원: {cnt}')

change = change%5000
cnt = change //1000
print(f'1000원: {cnt}')

change = change%1000
print(f'기타: {change}')
