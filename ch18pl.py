#ch18pl.py
#지역변수

def f():
    #지역변수 a
    a = 5
    print(f'지역변수 a: {a}')

#전역변수 a
a = 1
f()
print(f'전역변수 a: {a}')
