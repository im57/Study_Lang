#에러
'''
구문에러(syntax error) - 문법에러
ex)문자열에서 '하나만, if문에서 :말고 ;사용
'''


#예외 - 입력에 따라 발생 가능
'''
ex)변수 선언 없이 출력, 0으로 나누기, 리스트에서 인덱스에러

try:
    예외 발생 가능 라인
except 예외종류:
    에외처리 문장
except 예외종류:
    에외처리 문장
else:
    예외가 발생하지 않은 경우 수행
finally:
    예외 발생 유무에 상관없이 try 블록 이후 수행할 문장

'''

a=int(input('a: '))
b=int(input('b: '))

try:
    c=a/b
    print(c) #c=a/b에 문제 생기면 실행 안됨
except ZeroDivisionError:
    print('Cannot divide by 0')


a=5
b=0
L=[1,2,3]

try:
    c=a/b #ZeroDivisionError #여기만 실행되고 except로 넘어감
    print(x) #NameError
    print(L[3]) #IndexError
except ZeroDivisionError:
    print('cannot divide by zero')
except NameError:
    print('no variable named')
except IndexError:
    print('out of indexing in list')
else:
    print('else part') #예외 없을 때만 실행
finally:
    print('finally') #무조건 실행
