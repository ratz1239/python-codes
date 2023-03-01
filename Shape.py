class Shape:
    pub=10
    _pro=11
    __pri=12
    def __init__(self,l,b,h):
        print("This Is Constructor Of Class Shape")
        self.l=l
        self.b=b
        self.h=h
    def area(self):
        area=self.l*self.b
        print("Area Is:",area)
    def volume(self):
        volume=self.l*self.b*self.h
        print("Volume Is:",volume)
    #def volumes():

class Rectangle(Shape):
    def __init__(self,l,b,h):
        print("This Is Constructor Of Class Rectangle")
        super().__init__(l,b,h)
class Square(Shape):
    def __init__(self,l,b,h):
        print("This Is Constructor Of Class Square")
        super().__init__(l,b,h)

A1=Rectangle(10,20,5)
B1=Square(5,5,5)
#C1=Shape(1,2,3)
#del A1         To Delete An Object
A1.area()
A1.volume()
B1.area()
B1.volume()

'''
#rect=Rectangle(1,2,3)
#squa=Square(1)

d=A1.__dict__
for i in d:
        print({i:d[i]})

#A1=area()
#A1=volume()

#B1=area()
#B1=volume()

#print(C1._Shape__pri)          To Use Private Variable
'''
