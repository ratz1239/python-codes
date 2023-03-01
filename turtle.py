import pickle as p
l=[]
#-----------------------------------------------------    
def insert(l):
    temp=int(input("Enter Number To Be Added:"))
    l.append(temp)
    a=open('stack.dat','wb')
    p.dump(l,a)
    a.close()
#-----------------------------------------------------
def delete():
    a=open('stack.dat','rb')
    l=p.load(a)
    a.close()
    l.pop()
    a=open('stack.dat','wb')
    p.dump(l,a)
    a.close()
#-----------------------------------------------------    
def display():
    a=open('stack.dat','rb')
    l=p.load(a)
    a.close()
    l=l[::-1]
    for i in range(0,len(l)):
        print(l[i])
#-----------------------------------------------------    
while True:
    print("\n\t","Choose Any Option.\n")
    print("1.Insert Element\n2.Delete Element\n3.Display\n4.Exit\n")
    ch=int(input())
    if ch==1:
        insert(l)
    elif ch==2:
        delete()
    elif ch==3:
        display()
    else:
        break
