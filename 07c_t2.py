

input('준비되면 엔터를 누르세요')

start = time.time()

input('5초 센 후 엔터를 누르세요')
end=time.time()

et =int(end-start)
t =abs(5-et)

print(f'실제시간: {et초}')
print(f'5초와의 차이: {t초}')
