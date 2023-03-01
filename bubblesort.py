l=[5,4,8,2,10]
t=0
lt=len(l)
for i in range(0,lt):
    for j in range(0,lt-i-1):
        if l[j]>l[j+1]:
            t=l[j+1]
            l[j+1]=l[j]
            l[j]=t
print(l)            
