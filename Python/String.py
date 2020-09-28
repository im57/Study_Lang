#긴 문자열에서는 엔터필요할 때 \ 입력필요
sentence = 'Pthon is the \
most popular programming \
language in these days.'
print(sentence)

#''' """ 은 모양 그대로 사용 가능해짐
print("""Dear Alice,
Hi! How R U??
Bye~
From IM""")

''' 에러
print("Dear Alice,
Hi! How R U??
Bye~
From IM")
'''

#문자열 인덱싱
'''
 h  e  l l o   w o r l d
 0  1  2 3 4 5 6 7 8 9 10
-11-10-9-8-7-6-5-4-3-2 -1
'''
greeting = 'hello world'
print(greeting[0])
#greeting[0] = 'H' -> 불가

#문자열 슬라이싱
print(greeting[0])
print(greeting[0:5]) #0-4까지 문자열 == greeting[:5]
print(greeting[0:5:1]) #0-4까지 1간격
print(greeting[5:0:-1]) #5-1까지 -1간격
print(greeting[5:-1:1]) #5-(-1)까지(5-10) 1간격
print(greeting[:]) #문자열 전체
print(greeting[::]) #문자열 전체

#문자열 연결, 반복
a='hello'
b='world'
c=95
print(a+b)
print(a+str(c)) #숫자를 문자열로 변환
print(a*3) #a를 3번 반복
print(len(a)) #a 길이
print('h' in a) #a에 h 있나
print('w' not in a) #a에 w 없나

#문자열 메소드 - 문자열.메소드()형태
'''
upper() - 대문자로 변경
lower() - 소문자로 변경
isupper() - 모두 대문자인지 확인
islower() - 모두 소문자인지 확인
capitalize() - 첫 문자를 대문자로 변경
title() - 문자열의 각 단어의 첫문자들을 대문자로 변경
istitle() - 문자열의 각 단어의 첫문자들이 대문자인지 확인
count() - 부분문자열 카운트
find() - 부분 문자열 찾아 첫 인덱스 알려줌
join(list) - 리스트에 있는 자료들을 문자열로 연결
split() - 문자열을 스페이스 기준으로 잘라서 리스트에 저장
'''
state='mississippi'
print(state.count('s')) #4
print(state.count('ssi')) #2
print(state.count('s',5)) #[5:] - 2
print(state.count('s',1,5)) #[1:5] - 2
print(state.find('s')) #2
print(state.find('i',5)) #[5:] - 7
friends=['alice','bob','cindy']
print('-'.join(friends))
lists='alice bob cindy'
lists2='alice/bob/cindy'
print(lists.split()) - 스페이스 기준 분리
print(lists2.split('/')) - / 기준 분리
