#파이썬 구성요소 - modules + classes + built-in-functions(내장함수)

#모듈 - 코드들을 한 단위로 묶어 사용할 수 있게 하는 하나의 단위
'''
표준모듈-파이썬 패키지 안에 포함된 모듈
사용자모듈-사용자가 만드는 모듈
써드파티모듈-개인이 만들어서 제공하는 모듈

->코드의 재 사용성
->서로 다른 모듈에 같은 이름의 메소드가 있어도 충돌 안 생김

-import후 사용 ... ex)import math
-모듈내 함수 알고 싶으면 dir(모듈)
'''

#모듈 사용 방법
'''
1.
import 모듈
모듈.함수

ex)
import math
math.pow(2,5)

2.
from 모듈 import 함수

ex)
from math import pow, sqrt #pow, sqrt만 사용 가능 (모든 함수 -> import *)
pow(2,5)

3.
import 모듈 as <alias>

ex)
import math as mt
mt.pow(2,5)

'''

#모듈 만들기
'''
데이터, 함수들로 구성된 파일 만들기
파일명이 모듈명이

ex)
모듈파일 calc.py
------
"""연산에 필요한 함수들을 모아놓은 연산모듈이다"""

data=100

def add_all(a,b,c):
    total=a+b+c
    return total
    
def multiply_all(a,b,c):
    result=a*b*c
    return result

----------------
수행할 파일 practice.py
------
import calc

x=10;y=20;z=5

ans1=calc.add_all(x,y,z)
ans2=calc.multiply_all(x,y,z)

print(ans1,ans2)
print(calc.data)


'''

#random 모듈 - 임의의 값을 선택하는 함수들로 구성된 모듈
'''
정수선택
randint(a,b) - a<=N<=b 사이의 임의의 정수 N 선택
randrange(,,) - range()결과 중 임의의 값 선택

실수선택
random() - 0.0<=F<1.0 사이의 임의의 실수 F 선택
uniform(a,b) - a와 b 사이의 임의의 실수 선택

군집자료형에서 선택
choice(X) - 군집 자료형 X에서 임의의 원소 선택
sample(X,k) - 군집자료형 X에서 k개의 원소를 임의로 중복없이 선택
shuffle(X) - 군집자료형 X를 섞는다. immutable 자료형에서는 적용 불가
'''
import random
print(random.randint(10,20)) #10<=N<=20
print(random.randrange(5,15,2)) #range(5,15,2) ... 5-14 2간격
#random.randrange(20) for i in range(10) - 10번 중복 허용하여 0-19랜덤 뽑기
print(random.sample(range(20),10)) #중복없이 0-19중 10개 뽑기

print(random.random()) #0<=F<1
print(random.uniform(3,4)) #3<F<4

L=[0,1,2,3,4,5,6,7,8,9]
print(random.choice(L))
print(random.sample(L,3)) #3개 중복없이
random.shuffle(L)
print(L)

T=(0,1,2,3,4,5,6,7,8,9)
print(random.choice(T))
print(random.sample(T,3)) #3개 중복없이
#random.shuffle(T) - immutable은 불가

s='abcdefg'
print(random.choice(s))
print(random.sample(s,3)) #3개 중복없이
#random.shuffle(s) - immutable은 불가

