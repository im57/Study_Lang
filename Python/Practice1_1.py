#실습1

korean=int(input('국어 성적을 입력하세요 : '))
math=int(input('수학 성적을 입력하세요 : '))
english=int(input('영어 성적을 입력하세요 : '))

print('\n입력받은 성적')
print('------------') #print('-'*15)

print('국어 성적 : %d' % (korean)) # print('국어 성적 : ', (korean))
print('수학 성적 : %d' % (math))
print('영어 성적 : %d' % (english))
print('\n------------\n')

sum = korean+math+english
avg = float(sum/3)

print('총점 : %d' % (sum))
print('평균 : %.2f' % (avg))
