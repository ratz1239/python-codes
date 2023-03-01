l=[3,4,1,-2,10]
t=0
lt=len(l)
for i in range(0,lt):
    n=l[i]
    j=i-1
    while j>=0 and n<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=n
print(l)    
