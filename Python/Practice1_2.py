#실습2

radius=int(input('반지름을 입력하시오 : '))

print('반지름 : ', radius)

pi=3.141592

area=radius*radius*pi # area = pi * pow(radius, 2) -제곱
circum=2*radius*pi

print('원의 넓이 : %7.3f'% (area))
print('원의 둘레 : %.3f'% (circum))
