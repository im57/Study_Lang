#함수 
'''
내장 함수 - 파이썬에서 미리 만들어 제공하는 함수들
dir(__builtins__)라고 입력하면 내장함수 목록 볼 수 있음

사용자 정의 함수 - 사용자가 직접 정의
'''

#군집자료형에 유용한 함수
'''
len(), max(), min(), sum(), sorted(), reverse()
*sorted->결과 리스트
*reverse->순서 있는 군집자료형(list, tuple, str)에만 적용 가능 .. 결과 리스트
'''

#함수 정의
'''
def 함수명(파라미터):
    """이 함수는 두 정수에서 큰 값을 찾아서 반환하는 함수이다.""" #함수 설명
    -
    -
    return 반환값

'''
def find_max(a,b): #a,b-매개변수
    if a>b:
        y=a
    else:
        y=b
    return y

#함수 호출
m = find_max(10,20) #20 #10,20-인수
print(m)


#인수, 반환값 없는 함수
def hello():
    print('hello world')
    print('hello pytjon')
#main - 여기부터 프로그램 수행 시작
hello() #hello함수 실행


#반환 값이 여러개면 튜플로 묶어서 반환
def add_mul(x,y):
    sum=x+y
    mul=x*y
    return sum, mul #튜플로 반환

a=10;b=5
m,n=add_mul(a,b) #(15,50)
print(m,n)

#함수의 위치 - 호출 전에 정의되어 있어야 함
#main 표시 따로 없음
