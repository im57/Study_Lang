#실습1

time=int(input('근무 시간을 입력하세요: '))
salary=int(input('시간당 수당을 입력하세요: '))

if time>12:
    add=salary*0.3
    total=12*salary + (time-12)*(add+salary)
else:
    total=time*salary
    
print('총 급여는 %d 원 입니다.'%(total))
