s=''
g=''
a=open('asd.txt','r')
s=a.read()
for i in s:
    if i not in 'aeiouAEIOU':
        g+=i
#a.seek(56)
print(g)
#print(a.tell())
#s=s.strip('a')
#print(s)
a.close()

