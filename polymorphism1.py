class Shape:
    pub=10
    _pro=11
    __pri=12
    def __init__(self,l,b,h):
        print("This Is Constructor Of Class Shape(Rect)")
        self.l=l
        self.b=b
        self.h=h
    def __init__(self1,s):
        print("This Is Constructor Of Class Shape(Squa)")
        self.s=s
    def area(self):
        area=self.l*self.b
        print("Area Is:",area)
    def area(self1):
        area=self1.s*self1.s   
        print("Area Is:",area)
    def volume(self):
        volume=self.l*self.b*self.h
        print("Volume Is:",volume)
    def volume(self1):
        volume=self1.s*self1.s*self1.s
        print("Volume Is:",volume)

class Rectangle(Shape):
    def __init__(self,l,b,h):
        print("This Is Constructor Of Class Rectangle")
        super().__init__(l,b,h)
class Square(Shape):
    def __init__(self1,s):
        print("This Is Constructor Of Class Square")
        super().__init__(s)

A1=Rectangle(10,20,5)
B1=Square(5)


A1.area()
A1.volume()
B1.area()
B1.volume()
