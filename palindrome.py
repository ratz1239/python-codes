a=0
n=int(input("Enter Number:"))
N=n
while n>0:
    b=n%10
    n=n//10
    a=(a*10)+b
if a==N:
    print("Palindrome")
else:
    print("Not Palindrome")

