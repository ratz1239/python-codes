d={}
for i in range(0,3):
    i=input("Enter Name:")
    d[i]=int(input("Enter Marks:"))
print(dict(sorted(d.items(),key=lambda i:i[1])))    
