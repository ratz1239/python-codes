s1=input("Enter First String:")
s2=input("Enter Second String:")
d1={}
d2={}
l1=[]
l2=[]
s3=''
for i in s1.split(" "):
    d1[i]=1
for i in s2.split(" "):
    d2[i]=2
l1=d1.keys()
l2=d2.keys()
for i in l1:
    if i in l2:
        print(i)
