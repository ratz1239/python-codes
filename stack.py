l=[]
def push(l):
    t=list(input("Enter Element To Be Added:"))
    l+=t
    print("Element Added")
def pop(l):
    l.pop(len(l)-1)
    print("Element Deleted")
def display(l):
    r=l[::-1]
    print("\n")
    for i in r:
       print(i,end="\n")
    print("\n")
while True:
    print("1.Push\n2.Pop\n3.Display\n4.Exit")
    ch=int(input())
    if ch==1:
        push(l)
    elif ch==2:
        pop(l)
    elif ch==3:
        display(l)
    else:
        break
print("END")    
