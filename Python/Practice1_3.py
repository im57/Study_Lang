#실습3

nums=int(input('다섯 자리 숫자를 입력하시오 : '))

print()

one=nums//10000
et=nums%10000
two=et//1000
et=et%1000
three=et//100
et=et%100
four=et//10
five=et%10

print('%d, %d, %d, %d, %d'% (one,two,three,four,five))
print(one, ',', two, ',', three, ',', four, ',', five)
print('끝내려면 엔터를 누르세요.')
input()
