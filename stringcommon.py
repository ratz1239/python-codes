s1=input("Enter First String:")
s2=input("Enter Second String:")
d={}
for i in s1.split(" "):
    d[i]=1
print(d)
print("Common Words:",d)
