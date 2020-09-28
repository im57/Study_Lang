#실습3
'''
n1=int(input('정수를 입력하시오 : '))
n2=int(input('정수를 입력하시오 : '))
n3=int(input('정수를 입력하시오 : '))
n4=int(input('정수를 입력하시오 : '))
n5=int(input('정수를 입력하시오 : '))

nums=[n1, n2, n3, n4, n5]

max = nums[0]
i = 1
while i < 5:
    if max < nums[i]:
       max = nums[i]
    i+=1

print()
print('가장 큰 값 :', max)
'''

n=int(input('정수를 입력하시오 : '))
max=n

i=1
while i < 5:
    n=int(input('정수를 입력하시오 : '))
    if max < n:
       max = n
    i+=1
    
print()
print('가장 큰 값 :', max)
