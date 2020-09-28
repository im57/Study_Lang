#range() - 일정 범위의 수 반
'''
range(b) - 0부터 b-1까지의 수 반환
range(a,b) - a부터 b-1까지의 수 반환
range(a,b,n) - a부터 b-1까지의 n간격 수 반
'''

A=range(5)
print(type(A)) # range
print(A) # range(0,5)
B=list(range(5))
print(type(B)) #list
print(B) #[0,1,2,3,4]

#for
'''
#데이터 집합에서 데이터를 하나씩 변수에 넣고 반복 수행
for 변수 in [데이터집합]: #데이터집합 - range()함수,문자열,리스트,튜플,집합,사전
    -
    -
    -
'''

#range()함수
for x in range(5):
    print(x) #0 1 2 3 4 (공백이 아니라 엔터)

#문자열
for letter in 'PYTHON':
    y=letter.lower()
    print(y) #p y t h o n

#리스트
for x in [1,3,5,7,9]:
    print(x) #1 3 5 7 9

#사전
score={4:90, 2:80, 1:95, 5:88, 3:92}
for x in score:
    print(x) #1 2 3 4 5

for x in score.keys():
    print(x) #1 2 3 4 5

for x, y in score.items():
    print(x, y) #1 95 2 80 3 92 4 90 5 88

for x in score.values():
    print(x) #95 80 92 90 88


#리스트 안에 for 반복문 사용 ... for x in 데이터집합if조건
#A={x^2 | x ∈ {0,1,2,3,...,9}}
A=[x**2 for x in range(10)] #x의 제곱들
print(A)

#B={1,2,2^2,2^3,...,2^10}
B=[2**x for x in range(11)] #2의 x제곱들
print(B)

#C={x | x ∈ A and x is even}
C=[x for x in A if x%2==0]
print(C)


'''
군집 자료형 형 변환
str(A) - A를 문자열로 변환
list(A) - A를 리스트로 변환
tuple(A) -A를 튜플로 변환
set(A) - A를 집합으로 변환
dict(A) - A를 사전으로 변환
사전->다른자료형 ... 키를 이용해서 만듦
'''
A=[1,2,3,4]
B=(1,3,5)
C={2,4,6,8}
D={1:90,2:88,3:93}

E=tuple(A)
print(E) #(1,2,3,4)
F=set(B)
print(F) #{1,3,5}
G=list(C)
print(G) #[2,4,6,8]
H=list(D)
print(H) #[1,2,3]
I=tuple(D)
print(I) #(1,2,3)
J=set(D)
print(J) #{1,2,3}

