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
