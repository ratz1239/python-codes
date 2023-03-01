f=0
n=int(input("Enter Number:"))
for i in range (2,n):
    if n%i==0:
        f=1
if f==1:
    print("Not A Prime Number")
else:
    print("Prime Number")
    
