s=input("Enter String:")
s1=''
l=len(s)
for i in range (0,l+1):
    s1=s[i:]+s[:i]
    print(s1)
