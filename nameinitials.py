s=input("Enter String:")
l=len(s)
for i in range(0,l):
    if s[i].isupper() is True:
        print(s[i],end='.')

