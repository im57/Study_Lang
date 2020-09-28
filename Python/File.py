#open() 내장 함수
'''
파일객체 = open(file, mode)
file-파일명
mode-파일 열 때의 모드 ... r(읽기.디폴트),w(쓰기),a(쓰기+이어쓰기),r+(읽기+쓰기)

open후 사용 가능한 메소드
읽기
read()-파일 내용을 모두 읽어서 문자열로 반환
read(n)-n바이트 읽어서 문자열로 반환
readline()-한 줄씩 읽어서 문자열로 반환
readlines()-파일 전체를 리스트로 반환
쓰기
write()-문자열을 파일에 저장
writelines()-문자열 리스트를 파일에 저장

'''

f=open('newfile.txt','r')
a=f.read(4)
print(a)
b=f.read() #위에서 읽고 나머지 모두
print(b)
f.close() #파일 연결 끊기

print('-'*10)

f=open('about.txt','r')
a=f.readline()
print(a)
b=f.readline() #위에서 읽고 다음 줄
print(b)
f.close()

print('-'*10)

f=open('about.txt','r')
for line in f:
    print(line)
f.close()

print('-'*10)


f=open('about.txt','r')
a=f.readlines() #리스트로 반환 [,,,]
print(a)
f.close()

print('-'*10)

f=open('score.txt','r')
score=[]
for line in f:
    score.append(int(line))
print(score)
f.close()

print('-'*10)
#위와 동일
score=[]
with open('score.txt') as f:
    for line in f:
        score.append(int(line))
print(score)
f.close()

print('-'*10)

#사전형태 (값이 리스트)
D={}
with open('ban.txt') as f:
    for line in f:
        items=line.split()
        key,values=items[0],items[1:]
        D[key]=values
for key,val in D.items():
    print(key, val)
f.close()

print('-'*10)
f=open('subject.txt', 'w')
f.write('hello wolrd\n')
f.write('godd bye')
print('write subject.txt')
f.close()


print('-'*10)
f=open('subject2.txt', 'w')
f.writelines(['hello wolrd\n','bye bye'])
print('write subject2.txt')
f.close()


