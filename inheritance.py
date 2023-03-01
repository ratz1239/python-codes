class A:
    def __init__(self,name,age):
        self.name=name
        self.__age=30

    def display(self):
        print(self.name)
        print(self.age+100)

class B(A):
    def __init__(self,name,age,marks,ad):
        A.__init__(name,age)
        self.name=name+' Gupta'
        self.age=age+200
        self.marks=marks
        self.ad=ad

    def Display(self):
        
        print(self.marks)
        print(self.ad)

r=B('arpit',100,10,'123lbn')
#r.name='arpit'
#r.age=20
r.display()
#r.Display()
#R=A()
'''
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_rectangle(self,length, width):
        self.length = length
        self.width  = width

    def get_area(self):
        return self.length * self.width;

#sub class
class Box(Rectangle):

    def __init__(self, length, width, height):
        Rectangle.__init__(self,length,width)
        self.height = height

    def set_box(self,length, width, height):
        self.set_rectangle(length,width)
        self.height = height

    def get_volume(self):
        return self.get_area() * self.height
    
#creating object
b = Box(12,9,10)
print("Volume is ", b.get_volume())
b.set_box(12.5, 10.5, 9.5)
print("Volume is ", b.get_volume())
'''
