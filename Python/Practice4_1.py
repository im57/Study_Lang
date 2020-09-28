#실습1

def calculate(time,sal):
    total = time*sal

    if time > 12:
        total += (time-12)*sal*0.3

    return total
    

#main

time=int(input('근무 시간을 입력하세요: '))
sal=int(input('시간당 수당을 입력하시오: '))

total=calculate(time,sal)

print()
print('총 급여는',int(total),'원 입니다.')
