'''
mutable - list, set, dictionary .. 값 변경 가능
immutable - 문자열, tuple ... 값 변경 불가
'''

#Set - 중복 데이터 불가, 순서 없음 ... 인덱스,+,* 불가 ... mutable
s={1,2,5}
print(s)

#빈 집합
S=set()
D={}
print(type(S)) #set
print(type(D)) #dict

'''
add(x) - 원소 추가
clear() -  공집합으로 만들기
copy() - 복사
discard(x) - 원소 삭제.. 없는 원소 삭제하려고 해도 에러 발생 안 함
pop() - 임의의 원소 하나 가져오고 삭제 ... 어떤 원소인지 알 수 없음
remove(x) - 원소 삭제 .. 없는 원소 삭제하려고 하면 에러 발생
'''

A={8,4,2,6,5}
print(A) #순서 이상함
A={1,1,2,2}
print(A)
A={1,2,3,5,9}
A.discard(8)
print(A)
#A.remove(8) - 에러
A.pop() #임의의 원소 삭제
print(A)



#Dictionary - 집합의 일종 ... +,*사용 불가하지만 인덱스는 사용 ... (키:값)
#사전의 키 - mutable자료형은 키가 될 수 없음(리스트,집합,사전)
number={1:25,2:30,3:27}
print(number)

#빈 사전
D={}
print(type(D)) #dict

color={'red':2,'blue':3,'green':5}
print(color)
color['yellow']=8 #추가
print(color)
color['red']=5 #수정
print(color)
del color['green'] #삭제
print(color)
print(len(color)) #3
print('blue' in color) #True
print('green' not in color) #True

'''
clear() - 사전 내용 지움
copy() - 사전 복사
items() - 모든 데이터 (키,값) 반환
keys() - 키만 반환
values() - 값만 반환
update(D) - 사전 D를 추가
'''

D={'red':2,'blue':3,'green':5, 'yellow':8}
print(D)
D.clear()
print(D)
D={'red':2,'blue':3,'green':5, 'yellow':8}
print(D)
D2={'pink':1,'black':2}
D.update(D2)
print(D) #{'red':2,'blue':3,'green':5,'yellow':8,'pink':1,'black':2}

D={'red':2,'blue':3,'green':5}
A=D.items()
print(A) #dict_items([('red', 2), ('blue', 3), ('green', 5)])
B=list(D.items())
print(B) #[('red', 2), ('blue', 3), ('green', 5)]
A=D.keys()
print(A) #dict_keys(['red', 'blue', 'green'])
B=list(D.keys()) 
print(B) #['red', 'blue', 'green']
A=D.values()
print(A) #dict_values([2, 3, 5])
B=list(D.values()) 
print(B) #[2, 3, 5]
