l=0
s=0
while True:
    n=int(input("Enter Number:"))
    if l==0 and s==0:
        l=n
        s=n
    if l<n:
        l=n
    elif s>n:
        s=n
    o=input("Do You Want To Continue(Y/N):")
    if o=='N'or o=='n':
        break
print("Largest:",l)
print("Smallest:",s)
