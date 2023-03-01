import random
import pickle as p
import os as o
import time
import getpass
clrscr=lambda:o.system('cls')
d={}
#-------------------------------------------------------------------------
def random_pw():
    global spc
    global charc
    global chars
    global num
    pw=''
    for i in range(0,4):
        tspc=random.choice(spc)
        tcharc=random.choice(charc)
        tchars=random.choice(chars)
        tnum=random.choice(num)
        pw+=tspc+tcharc+tchars+tnum
    return pw
#-------------------------------------------------------------------------
def dump_rec(email,pw):
    a=open("LOGIN.dat","rb")
    d=p.load(a)
    a.close()
    
    d[email]=pw
    a=open('LOGIN.dat','wb')
    p.dump(d,a)
    a.close() 
    print("DONE")   
#-------------------------------------------------------------------------
def pw():
    global spc
    global charc
    global chars
    global num
    countspc=0
    countc=0
    counts=0
    countn=0
    pw=getpass.getpass()
    for i in range(0,len(pw)):
        if pw[i] in spc:
            countspc+=1
        elif pw[i] in charc:
            countc+=1
        elif pw[i] in chars:
            counts+=1
        elif pw[i] in num:
            countn+=1
    #print(countspc,countc,counts,countn)
    t={"Special Characters":countspc,"Capital Letters":countc,"Small Letters":counts,"Numbers":countn}
    tv=t.values()
    tv=list(tv)
    tk=t.keys()
    tk=list(tk)
    for i in range(0,len(tv)):
        if tv[i]<1:
            print("Not Enough",tk[i],"In Your Password")
    return pw        
#-------------------------------------------------------------------------
spc=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','|','}',']','{','[',':',';','/','?',',','<','>','`','~','.']
charc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=["1","2","3","4","5","6","7","8","9","0"]
#-------------------------------------------------------------------------
def email():
    f=0
    count=0
    global spc
    email=input("Enter Your Email ID:")
    t=email[::-1]
    for i in range(0,len(t)):
        if t[i]!='@':
            count+=1
        else:
            break
    #print(counta)
    l=len(email)
    for i in range(0,l-count-1):
        if email[i] in spc:
            f=1
            g=email[i]
    if f==1:
        print("Error Occured")
        print("You Used Special Character",g)
    else:        
        print("Email ID Is Good To Go")
        return email
#-------------------------------------------------------------------------
print("######################## PASSWORD GENERATOR ########################")

print("Choose From The Following:\n1.Create Your Own Password\n2.Generate Random Password")
ch=int(input())
if ch==1:
    email=email()
    pw=pw()
    dump_rec(email,pw)
    print("Email And Password Created")
else:
    email=email()
    pw=random_pw()
    print("Password Created Is:",pw)
    time.sleep(5)
    clrscr()
    dump_rec(email,pw)
    print("Email And Password Created")
a=open('LOGIN.dat','rb')
d=p.load(a)
for i in d:
    print("Email:",i,'\n',"Password:","*"*len(d[i]),sep="")
a.close()
print("END")
