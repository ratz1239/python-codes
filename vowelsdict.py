s=input("Enter String:")
d={'a':'#','e':'@','i':'$','o':'%','u':'!'}
l=list(s)
for i in range(0,len(l)):
    if l[i] in d:
        l[i]=d[l[i]]
print(l)        
