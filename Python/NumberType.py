#수치자료형

#정수자료형
x=100
y=200 #x=100;y=200
print(x,y)

x=10
y=4
print(x/y) #나누기
print(x//y) #몫
print(x%y) #나머지
print(2**2) #2의 2제곱

print(2**3**2) #2**9
print((2**3)**2) #8**2
print(2**3*2) #8*2
print(2*3**2) #2*9

#실수자료형
a=10.5
b=11.
c=.5
print(a,b,c)

print(2.5e5) # 2.5 * 10의 5제곱
print(3.25E-4) #3.25 * 10의 -4제곱

a=10
b=20.
c=a+b
print(c)
type(c) #float

#복소수자료형
x=5+10j
print(x.real) #실수부
print(x.imag) #허수부
print(x.conjugate())  #켤레복소수-가운데 부호만 변경



#자료형변환
a=int(5.6) #5
b=int(-2.9) #-2
c=int('15') #15
print(a,b,c)

x=float(3)
y=float('15.7')
z=float('15')
print(x,y,z)


#수치 연산 함수
'''
abs(x)-x의 절대값
divmod(x,y)-(x//y, x%y)반환
pow(x,y)-x의y제곱 반
'''

print(abs(-3))
print(divmod(5,2))
print(pow(3,2))

#math 모듈
import math
print(math.fabs(-5)) #절대값
print(math.pow(2,5)) #몫, 나머지
print(math.sqrt(9)) #루트
print(math.floor(4.5)) #4.5이하 정수 중 가장 큰 정수
print(math.ceil(4.5)) #4.5이상 정수 중 가장 작은 정수
