#실습3

d1={'ko':80,'en':90,'ma':86}
d2={'ko':78,'en':88,'ma':85}
d3={'ko':85,'en':85,'ma':92}
d4={'ko':70,'en':69,'ma':65}
d5={'ko':90,'en':95,'ma':100}

L=[d1,d2,d3,d4,d5]

for i in range(5):
    print(i,'번:', sum(L[i].values()) / len(L[i].values()))


'''
score={1:[80,90,86], 2:[78,88,85], 3:[85,85,92], 4:[70,69,65], 5:[90,95,100]}

for key,value in score.items():
    print(key,'번:', sum(value)/3)

''' 


