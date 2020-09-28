#실습2

def temC_to_temF(celsius): 
    return celsius *9 /5 +32

#main

start=int(input('시작 온도를 입력하시오: '))
end=int(input('끝 온도를 입력하시오: '))

print()
for celsius in range(start,end+1):
    fahrenheit = temC_to_temF(celsius)
    print('섭씨 %.2f도는 화씨 %.2f도입니다.' % (celsius, fahrenheit))
