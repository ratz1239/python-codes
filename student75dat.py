import pickle as p
import os as o

d={}
#-------------------------------------------------
def dump_rec():
    a=open('STUDENT.dat','wb')
    p.dump(d,a)
    a.close()
#-------------------------------------------------
def append_rec():
    a=open('STUDENT.dat','rb')
    r=p.load(a)
    a.close()
    for i in d:
        r[i]=d[i]
    a=open('STUDENT.dat','wb')
    p.dump(r,a)
    a.close()
#-------------------------------------------------
def input_rec(d):
    adno=int(input("Enter Admission Number:"))
    name=input("Enter Name:")
    marks=int(input("Enter Marks:"))
    d[adno]=[name,marks]
    print("1.Write\n2.Append")
    choice=int(input())
    if choice==1:
        dump_rec()
    else:
        append_rec()
#-------------------------------------------------
def count_rec():
    count=0
    a=open('STUDENT.dat','rb')
    r=p.load(a)
    for i in r:
        if r[i][1]>75:
            count+=1
            print(i,r[i])
    print("No. Of Students Having Marks Above 75%:",count)
    a.close()
#-------------------------------------------------
while True:
    print("1.Create\n2.Display 75%\n3.Exit")
    ch=int(input())
    if ch==1:
        input_rec(d)
    elif ch==2:
        count_rec()
    else:
        break
