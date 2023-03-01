f=0
s=1
n=int(input("Enter Number Of Terms:"))
if n==1:
    print(f)
elif n==2:
    print(f,s)
else:
    print(f,s)
    for i in range (2,n):
        t=f+s
        print(t)
        f=s
        s=t
