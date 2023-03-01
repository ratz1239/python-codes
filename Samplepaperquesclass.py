class STUDENT:
    def __init__(self,name,rollno,m):
        self.name=name
        self.rollno=rollno
        self.marks=m
        self.avg=sum(m)/3
    def DISPLAY(self):
        print("Name:",self.name,"\nRollno:",self.rollno,"\nAverage Marks:",self.avg)
name1=input("enter name of 1")
name2=input("enter name of 2")
name3=input("enter name of 3")
r1=int(input("enter rollno of 1"))
r2=int(input("enter rollno of 2"))
r3=int(input("enter rollno of 3"))
m1=list([int (x) for x in input("enter marks of 1").split()])
m2=list([int (x) for x in input("enter marks of 2").split()])
m3=list([int (x) for x in input("enter marks of 3").split()])
a1=STUDENT(name1,r1,m1)
a2=STUDENT(name2,r2,m2)
a3=STUDENT(name3,r3,m3)

a1.DISPLAY()
a2.DISPLAY()
a3.DISPLAY()
