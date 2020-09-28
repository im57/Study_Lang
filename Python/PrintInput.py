#print
print('hello','world') #hello world - 자동으로 공벡 추가
print('hello'+'world') #helloworld

'''
\- 다음 줄과 연속
\' = '
\" = "
\\ = \
\n = 개행문자
\t = tab키
'''

#서식 출력 - %s(문자열) %d(정수) %f(실수) -> print(' ' % ())
#%a.bf - 소수점 포함 a칸 잡고 소수점 아래 b자리까지 출
name='Alice'
score=95
print('%s got %d score' % (name, score))
print('%10s got %5d score' % (name, score)) #10칸 잡아서 name, 5칸 잡아서 score 출

math=93.5;eng=88.3
print('Math is %5.2f and Eng is %6.3f' % (math,eng))

#print()함수는 상항 '\n' 자동 추가됨
#다른 문자 출력하고 싶으면 end=''추가..
a='hello world'
print(a, end='**')
print(a)


#input - 입력함수
x = input('Enter x: ') # x=int(input('Enter x: '))
print('x is %s'%(x))
print(type(x)) # 입력데이터는 항상 문자열
print('x + 10 is %d'%(int(x)+10)) #int()로 문자열을 숫자로 변환
