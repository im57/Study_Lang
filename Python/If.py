#if
'''
if 조건:
    -
    -
elif 조건 :
    -
    -
else :
    -
    -
-
-

'''
score = int(input('성적 : '))

if score>=90:
    if score >= 95:
        grade='A+'
    else :
        grade = 'A'
elif 80<=score:
    grade='B'
else :
    grade='C'
print(grade)
