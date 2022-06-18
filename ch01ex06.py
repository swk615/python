

an =int(input('아메리카노 판매수:'))
cn =int(input('카폐라떼 판매수:'))
pn =int(input('카푸치노 판매수:'))
s = an*2000+cn*3000+pn*3500
m_s = s*30
print()
print(f'일일 판매 매충액은 {s}입니다.')
print(f'한달 기준 예상 매출액은 {m_s}입니다.')
print()
p =int(input(' 예상 지출액을 입력하세요:'))
po = m_s - p
print(f'한달 예상 순이익은 {po}입니다,')

       



