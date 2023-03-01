#            Question No.2

t1=(1,2,5,7,9,2,4,6,8,10)
l=len(t1)
#Part (a)
print(t1[0:l//2],'\n',t1[l//2:l])

#Part (b)
t3=()
t3=list(t3)
for i in range(0,l):
    if t1[i]%2==0:
        t3.append(t1[i])
t3=tuple(t3)
print("The New Tuple With Even Values From Firstt Tupple:\n",t3)

#Part (c)
t2=(11,13,15)
newt=t1+t2
print("Concatenated Tuple Is:",newt)

#Part (d)
ma=max(t1)                                          
mi=min(t1)      
print("The Maximum Value From Tuple Is:",ma)
print("The Minimum Value From Tuple Is:",mi)