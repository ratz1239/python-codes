import random as r
import pickle as p
import os as o
dm=500
d={}
count=0
#------------------------------------------------------------------------
def players(pl):
    for i in range(1,pl+1):
        d[i]=0
    a=open('LUCKY7.dat','wb')
    p.dump(d,a)
    a.close()    
#--------------------------------------------------
def dump_rec(d):
    a=open('LUCKY7.dat','wb')
    p.dump(d,a)
    a.close()        
#------------------------------------------------------------------------
def money(dm,e):
    a=open('LUCKY7.dat','rb')
    d1=p.load(a)
    if e in d:
        d[e]=dm
    a.close()
    dump_rec(d)
#------------------------------------------------------------------------
def game(dm,e):
    print("                   Pick One                   ")
    print("1.Less Than 7\n2.Exact 7\n3.More Than 7")
    n=int(input())
    b=int(input("Enter Your Bet(Min. 100):"))
    if b>dm:
        print("Not Enough Money In Your Balance")
        
    print("*************************Game Started*************************")
    i=r.randint(1,14)
    print("Lucky Number Was:",i)
    if n==1:
        if i<7:
            print("You Won:Rs.",2*b)
            dm+=b
            print("Your Balance Now:",dm)
        else:
            print("You Lost:Rs.",b)
            dm-=b
            print("Your Balance Now:",dm)
    elif n==2:
        if i==7:
            print("You Won:Rs.",2*b)
            dm+=b
            print("Your Balance Now:",dm)
        else:
            print("You Lost:Rs.",b)
            dm-=b
            print("Your Balance Now:",dm)
    elif n==3:
        if i>7:
            print("You Won:Rs.",2*b)
            dm+=b
            print("Your Balance Now:",dm)
        else:
            print("You Lost:Rs.",b)
            dm-=b
            print("Your Balance Now:",dm)
    if dm<100:
        print("Balance Less Than Minimum Value")
        print("*************************GAME OVER*************************")
    money(dm,e)        
#------------------------------------------------------------------------
pl=int(input("Enter Number Of Players:"))
players(pl)
rd=int(input("How Many Rounds Do You Want To Play:"))
for t in range(1,rd+1):                     #t for rounds
    for e in range(1,pl+1):                 #e for players
        print("**************************************Player",e," Turn**************************************")
        if t==1:
            game(dm,e)
        else:
            game(d[e],e)
    print("****************************************************ROUND",t," OVER****************************************************")
    print("Your Scores:",d)
a=open('LUCKY7.dat','rb')
d2=p.load(a)
k=list(d2.keys())
v=list(d2.values())
m=max(d2.values())
p=v.index(m)
winner=k[p]
print("##################################################### Winner Of The Game Is:Player",winner," #####################################################")