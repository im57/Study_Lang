#실습2

score=[0,0,0,0,0]
max=0
min=0
sum=0
for i in range(5):
    score[i] = int(input('성적을 입력하시오: '))

    if i==0:
        max=score[i]
        min=score[i]
    else:
        if score[i]>max:
            max=score[i]
        elif score[i]<min:
            min=score[i]

    sum+=score[i]

avg=sum/5

print()
print('입력한 성적들: ', score)
print('최고 성적', max)
print('최저 성적', min)
print('평균', avg)

'''
score=[]
for i in range(5):
    data = int(input('성적을 입력하시오: '))
    score.append(data)

print()
print('입력한 성적들: ', score)
print('최고 성적: ', max(score))
print('최저 성적: ', min(score))
print('평균: %2f',%(sum(score)/len(score)))

'''
