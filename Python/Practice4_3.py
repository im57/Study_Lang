#실습3

def check(num):    
    if num == answer:
        print()
        print('빙고~~',count,'번 만에 맞혔습니다. 입력한 숫자는',num,'입니다.')
    elif num < answer:
        print('더 큰 숫자를 선택하세요.')
    elif num > answer:
        print('더 작은 숫자를 선택하세요.')

#main

import random

answer=random.randint(1,100)

n=int(input('숫자를 맞혀보세요(1-100): '))
count=1

check(n)

while answer!=n:
    n=int(input('숫자를 맞혀보세요(1-100): '))
    count += 1
    check(n)

print()
input('프로그램을 마치려면 엔터를 누르세요.')
