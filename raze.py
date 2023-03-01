import pickle as p

d={}
#--------------------------------------------------------------
class Student:
  #  def __init__(self,rno=0,name=''):
   #     self.rno=rno
    #    self.name=name
     #   self.m1,self.m2,self.m3=0.0,0.0,0.0

    def minput(self):
        self.rno=int(input("Enter Roll No:"))
        self.name=(input("Enter Name:"))
        print("Enter Marks Of 3 Subjects:")
        self.m1=float(input("Marks 1:"))
        self.m2=float(input("Marks 2:"))
        self.m3=float(input("Marks 3:"))
        d[s.rno]=[s.name,s.m1,s.m2,s.m3]
        dinput(d)
        
    def DISPLAY(self,d):
        print("\n\nStudent Details:-")
        print("Name:",self.name)
        print("Roll No.:",self.rno)
        print("Marks Of 3 Subjects:",self.m1,self.m2,self.m3,sep=" ")

s=Student()

#--------------------------------------------------------------
def dinput(d):
    a=open('coc.dat','rb')
    r=p.load(a)
    a.close()
    for i in d:
        r[i]=d[i]
    a=open('coc.dat','wb')
    p.dump(r,a)
    print(r)
    a.close()

#--------------------------------------------------------------
def display(d):
    a=open('coc.dat','rb')
    r=p.load(a)
    #s.DISPLAY(d)
    print(r)
    a.close()

#--------------------------------------------------------------
'''def add(d):
    
    s.minput()
    d[s.rno]=[s.name,s.m1,s.m2,s.m3]
'''

#--------------------------------------------------------------
while True:
    print("\n1.Input Details","\n2.Display Details","\n3.Exit")
    ch=int(input())
    if ch==1:
        s.minput()
        dinput(d)
    elif ch==2:
        display(d)
    else:
        break
