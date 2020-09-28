#객체 - 파이썬에서 모든 데이터, 모든 함수는 객체이다
#클래스 - 객체를 만들기 위한 도구, 세상의 모든 물체를 객체로 만들 수 있음
'''
클래스의 구성
속성 - 객체를 구성하는 데이터
메소드 - 속성에 대해 어떤 기능을 수행하는 함수
생성자,소멸자 - 객체 생성과 소멸시에 자동 호출되는 특별한 메소드
연산자 중복 - 연산자(+,-등) 기호를 이용하여 표현할 수 있도록 함

'''
#강아지 클래스
class Dog:
    """강아지를 이름과 나이로 표현하는 클래스"""
    """속성은 강아지 객체를 구성하는 데이터"""

    def __init__(self,name,age): #생성자 ... 강아지 객체 만들 때 자동 호출
        """강아지 객체를 생성하는 생성자 메소드"""
        self.name=name #속성
        self.age=age #속성

    def bark(self): #메소드
        print(self.name, 'is barking 멍멍')


x=Dog('Jack',3) #x객체 생성(name은 Jack age는 3)
y=Dog('Tom',2) #y객체 생성(name은 Tom age는 2)
x.bark()
y.bark()
print(x.name,'is',x.age,'years old.')
print(y.name,'is',y.age,'years old.')

print('-'*10)

#원 클래스
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        a=3.14*pow(self.radius,2)
        return a

    def perimeter(self):
        p=2*3.14*self.radius
        return p

x=Circle(5)
y=Circle(10)
print('x radius',x.radius)
print('x area:',x.area())
print('x perimeter:%.2f'%x.perimeter())
print('y radius',y.radius)
print('y area:',y.area())
print('y perimeter:%.2f'%y.perimeter())

print('-'*10)


#list 클래스
L=list([1,2,3]) #L=[1,2,3]
print(L)


#int 클래스
x=int(10) #x=10
y=5
z=x.__add__(y) #z=x+y
print(x)
print(z)
p,q,r=100,100,200
print(p.__eq__(q)) #p==q
print(p.__gt__(r)) #p>r

print('-'*10)


#연산자 중복
'''
수치 연산자 메소드
__add__(self,other) : +
__sub__(self,other) : -
__mul__(self,other) : *
__truediv__(self,other) : /
__floordiv__(self,other[,modulo]) : //
__mod__(self,other) : %
__pow__(self,other) : **
__gt__(self,other) : >
__ge__(self,other) : >=
__lt__(self,other) : <
__le__(self,other) : <=
__eq__(self,other) : ==
__ne__(self,other) : !=

'''

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def get(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other):
        newX=self.x+other.x
        newY=self.y+other.y
        return Point(newX,newY)
    

p1=Point(2,3)
p2=Point(4,7)
p3=p1+p2 #__add__(p1,p2)
print(p1.get())
print(p2.get())
print(p3.get())

print('-'*10)


#클래스와 모듈 - 클래스가 저장된 파일을 모듈로 사용 가능
#ex) 파일이름 Pet.py
'''
"""나의 애완동물 클래스"""

class Dog:
    """강아지 클래스"""
    def __init__(self,name,age): 
        self.name=name 
        self.age=age 

    def bark(self): 
        print(self.name, 'is barking 멍멍')

class Cat:
    """고양이 클래스"""
    def __init__(self,name,color): 
        self.name=name 
        self.color=color 

    def show_color(self): 
        print(self.name, 'is', self.color)

---

from Pet import Dog,Cat

a=Dog('Jack',3)
b=Dog('Daisy',2)

c=Cat('Kitty','white')
d=Cat('Molly','black')

a.bark()
b.bark()

c.show_color()
d.show_color()

'''
from Pet import Dog,Cat

a=Dog('Jack',3)
b=Dog('Daisy',2)

c=Cat('Kitty','white')
d=Cat('Molly','black')

a.bark()
b.bark()

c.show_color()
d.show_color()
