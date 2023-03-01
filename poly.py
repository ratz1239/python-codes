import math as m
class A:
    var=10
    _var=2
    __var=100
    def __init__(self):
        print("Class A")
        self.name="hello world"

    def area(self):
        print(self.name+self.name)
        
    def disp(self,name):
        print(self.name*3)
    def newv(self):
        print(self.var)
    def pri(self):
        self.__var=200
    def pro(self):
        return self.__var
class C(A):
    
    def __init__(self):
        self.age=5
        print("Class C")
        self.name="Hello"
        #super().__init__()
    def area(self):
        print(self.name)

    def area(self):
        print("Exit",self.age)

    def __add__(self):
        f=[1,2,3]
        f1=[4,5]
        print(f+f1)
    def s(self):
        f=[1,2,3]
        f1=[4,5]
        print(sum(f+f1))
    def disp(self,name,age):
        return f"{self.name} is {self.age}"
a1=A()
c1=C()
c1.__add__()
#a1.newv()
#c1.newv()


    
