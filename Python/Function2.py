#전역변수와 지역변수
'''
전역변수 - 프로그램 전체에서 사용 가능
지역변수 - 함수 내에서만 사용 가능

'''

#global 선언
'''
-전역변수를 함수 내에서 바꾸고자 할 때 필요
-함수에서 만든 지역변수를 전역변수로 사용하고자 할 때 필요

'''
def test():
    global a
    a=200
    print(a)

a=300
print(a) #300 
test() #200
print(a) #200
    

#mutable 객체가 인수 - list, set, dict -> L과 M이 하나의 객체를 공유
def test(M):
    M[2]+=2
    M[4]+=5

L=[10,20,30,40,50]
print(L) #10,20,30,40,50
test(L) #같은 객체 안 가르키게 하려면 test(L[:])해야함
print(L) #10,20,32,40,55


#기본값이 있는 인수 - 함수호출시 인수를 안 넘겨줘도 인수가 자신의 기본값 취함
def inc(a, step=1): #기본값 있는 인수가 먼저 올 수 없음 ... inc(step=1,a) ->오류
    return a+step

b=inc(10)
print(b) #11 ... step=1
c=inc(10,50)
print(c) #60 ... step=50

#키워드 인수
def area(x,y):
    return x*y

print(area(10,5))
print(area(x=10,y=5))
print(area(y=5,x=10)) #매개변수와 값을 같이 적으면 순서 상관 없음
print(area(10,y=5))
#print(area(5,x=10)) #x에 두개가 할당되어 오류
#print(area(x=10,5)) #일반 인수 뒤에만 키워드 인수 가능


#가변인수 - 인수 개수가 정해지지 않음
'''고정인수 나열 후 나머지를 마지막에 튜플형식으로 한번에 받음'''
def friends(*name):
    for n in name:
        print(n)

friends('sam','tom')
friends('cindy','paul','kate')

def arg(a,b,*c):
    print(a,b,c)
    print(sum(c))

arg(10,20) #10,20,() / 0
arg(7,8,9) #7,8,(9,) / 9
arg(1,2,3,4,5) #1,2,(3,4,5) / 12



#정의되지 않은 키워드 인수 ... **형식으로 기술 ..사전형식이 됨
def name_age(**list):
    print(list)

name_age(Alice=10,Paul=12) #{'Alice': 10, 'Paul': 12}
name_age(Kate=5,Sam=17,Tom=5) #{'Kate': 5, 'Sam': 17, 'Tom': 5}



#람다함수 - lambda 인수들 : 반환할 식
'''
이름 없는 한 줄짜리 함수
return문 사용 안 함
람다 함수의 몸체는 문이 아닌 하나의 식
함수를 함수 인자로 넘길 때 유용

ex)
def add(x,y):
    return x+y
    
->동일한 람다함수로

lambda x,y:x+y

'''

#map함수
'''
map(함수명, 함수에 대한 인수 집합)
'''
name=['Tom','Sam','Bob','Ten']
A=map(len,name)
print(list(A))

def func(x):
    return x*x
X=[1,2,3,4,5]
print(list(map(func,X))) #함수 func에 X의 값들을 하나씩 적용

print(list(map(lambda a:a*a, X))) #위 func함수와 동일


#filter함수
'''
filter(함수명, 함수에 대한 인수 집합) ... 함수-참/거짓 반환하는 함수
'''

print(list(filter(lambda a:a%2==1, range(11))))
