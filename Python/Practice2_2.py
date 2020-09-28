num=int(input('정수를 입력하시오 : '))

print()

i=1
count=0
while i <= num:
    if num % i == 0:
        print(i)
        count+=1
    i += 1

print()
print(num, '의 약수의 개수 :', count)
