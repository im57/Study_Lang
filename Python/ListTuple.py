#List - mutable ... score[0]=100 가능 ... 문자열은 불가능
score=[10,20,30]
print(score)

'''
append(x) - x를 리스트 끝에 추가
clear() - 리스트 비우기
copy() - 리스트 복사
count(x) - 데이터 x 개수 알아냄
extend(M) - 리스트 M연결
index(x) - x위치
insert(i,x) - i번째에 x추가
pop() - 리스트의 지정한 값 하나를 읽어 내고 삭제
remove(x) - x삭제
reverse() - 순서 역순
sort() - 리스트 정렬
'''
L=[1,2,3,4]
L.append(5)
print(L) #12345
L.insert(5,6)
print(L) #123456
L.pop()
print(L) #12345
L.pop(0)
print(L) #2345
L.remove(5)
print(L) #234
print(L.index(3)) #1
print(L.count(3)) #1

A=[]
A.append(1)
A.append(2)
A.append(3)
print(A)
A.clear()
print(A)

'''
M=L로 복사하면 같은 객체 가리키게됨... M[0]을 변경 -> L[0]도 변경
M=L.copy()로 복사하면 M[0]를 변경해도 L[0]에 영향없
'''
A=[1,2,3]
B=[1,2,3]
equalA=A
copyB =B.copy()
equalA[0]=5
copyB[0]=5
print(A)
print(equalA)
print(B)
print(copyB)

A=[1,3,5]
B=[2,4,6]
A.extend(B)
print(A)
A.sort()
print(A)
A.sort(reverse=True)
print(A)
A.reverse()
print(A)



#Tuple - immutable ... 한번 만들면 데이터 변경 불가
T=(1,3,5,7,9)
print(T)

'''
index(x) - x의 위치
count(X) - x의 개수
'''

#빈 튜플
T=()
T=tuple()

#원소가 하나인 튜플 - 콤마 필요 ... 콤마를 사용하면 괄호가 없어도 튜플로 인식
T=(1,)
print(type(T)) #tuple
T=(1) #T=1
print(type(T)) #int

A=1,2,3
print(type(A)) #tuple
A=1,
print(type(A)) #tuple

#튜플은 여러 변수에 값을 동시에 할당할 수 있도록 한다.
a,b,c = 1,2,3
print(a) #1
print(b) #2
print(c) #3

#튜플을 이용한 swap
x,y=10,20
print(x,y)
x,y=y,x
print(x,y)

