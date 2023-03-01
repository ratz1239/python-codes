import random as r
import pickle as p
import os as o
p1=1
p2=2
dm=500
d={}
count=0
#------------------------------------------------------------------------
def p1(dm1):
    print("Total Balance Of Player 1:",dm1)
    a=open('p1.dat','wb')
    p.dump(dm1,a)
    a.close()
    #return(dm1)
#------------------------------------------------------------------------
def p2(dm2):
    print("Total Balance Of Player 2:",dm2)
    a=open('p2.dat','wb')
    p.dump(dm2,a)
    a.close()
    #return(dm2)
#------------------------------------------------------------------------
def read_info1():
    a=open('p1.dat','rb')
    dp1=p.load(a)
    a.close()
    return(dp1)
#------------------------------------------------------------------------
def read_info2():
    a=open('p2.dat','rb')
    dp2=p.load(a)
    a.close()
    return(dp2)
#------------------------------------------------------------------------
def game(dm,t):
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
    global count
    if t>count:
        p1(dm)
        count+=1
    else:
        p2(dm)         
#------------------------------------------------------------------------
rd=int(input("How Many Rounds Do You Want To Play:"))
for t in range(1,rd+1):
    print("**************************************Player 1 Turn**************************************")
    if t==1:
        p1(dm)
        dm1=read_info1()
        game(dm1,t)
    else:
        dm1=read_info1()
        p1(dm1)
        game(dm1,t)    
    print("**************************************Player 2 Turn**************************************")
    if t==1:
        p2(dm)
        dm2=read_info2()
        game(dm2,t)
    else:
        dm2=read_info2()
        p2(dm2)
        game(dm2,t)
if dm1>dm2:
    print("****************************************************Player 1 Won****************************************************")
else:
    print("****************************************************Player 2 Won****************************************************")
def __init__():
    dm=500    