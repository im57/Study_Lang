#while
'''
while 조건식:
    -
    -
-
-

'''

a=1
while a<=5:
    print(a)
    a+=1
print('-'*10)

a=1
sum=0
while a<=10:
    sum+=a
    a+=1
print('sum: ',sum)
print('-'*10)


#break
a=1
while True:
    if a>5:
        break
    print(a)
    a+=1
print('-'*10)

#continue
a=1
while a<=10:
    if a%2==0:
        a+=1
        continue
    print(a)
    a+=1
print('-'*10)

i=2
while i <=9:
    j=1
    while j<=9:
        print('%3d'%(i*j), end='')
        j+=1
    print()
    i+=1
print('-'*10)

