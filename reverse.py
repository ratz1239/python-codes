a=0
n=int(input("Enter Number:"))
N=n
while n>0:
    b=n%10
    n=n//10
    b=b**3
    a+=b
if a==N:
    print("Armstrong")
else:
    print("Not Armstrong")

