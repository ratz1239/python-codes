import pickle as p
import os as o

d={}
#--------------------------------------------------
class BANK:
    def __init__(self):
        self.=
        self.=
        self.=
#--------------------------------------------------
def input_rec():
    accno=int(input("Enter Account Number:"))
    name=input("Enter Name:")
    pw=input("Enter Password(Very Important!!):")
    typech=int(input("1.Current\n2.Savings"))
    if typech==1:
        print("Enter Amount(Minimum Rs.1000):")
        amount=int(input())
        if amount>1000:
            d[accno]=[typech,name,pw,amount]
        else:
            print("ERROR!!Input Is Less Than Rs.1000")
    else:
        amount=0
        d[accno]=[typech,name,pw,amount]
    ca(d)
#--------------------------------------------------
def ca(d):
    l=o.listdir(r'C:\Users\ASUS\Downloads\Python Codes')
    if 'BANK.dat' in l:
        a=open('BANK.dat','rb')
        r=p.load(a)
        a.close()
        for i in d:
            r[i]=d[i]
        a=open('BANK.dat','wb')
        p.dump(r,a)
    else:
        a=open('BANK.dat','wb')
        p.dump(d,a)
    a.close()
#--------------------------------------------------
def chname(d):
    a=open('TEMP.dat','wb')
    p.dump(d,a)
    a.close()
    o.remove('BANK.dat')
    o.rename('TEMP.dat','BANK.dat')
#--------------------------------------------------
def da():
    a=open('BANK.dat','rb')
    d=p.load(a)
    taccno=int(input("Enter Account Number:"))
    if taccno in d.keys():
        tpw=input("Enter Password:")
        if tpw==d[taccno][2]:
            d.pop(taccno)
            return(d)
        else:
            print("Password Is Wrong")
    else:
        print("This Account Number Does Not Exist")
#--------------------------------------------------
def wm():
    a=open('BANK.dat','rb')
    d=p.load(a)
    taccno=int(input("Enter Account Number:"))
    if taccno in d.keys():
        tpw=input("Enter Password:")
        if tpw==d[taccno][2]:
            print("Your Current Balance:",d[taccno][3])
            tamount=int(input("Enter Amount To Be Withdrawn:"))
            if tamount>d[taccno][3]:
                print("Balance Not Enough")
            else:
                d[taccno][3]-=tamount
                print("Amount Withdrawn")
        else:
            print("Password Is Wrong")
    else:
        print("This Account Number Does Not Exist")
    a.close()
    return(d)
#--------------------------------------------------
def dm():
    a=open('BANK.dat','rb')
    d=p.load(a)
    taccno=int(input("Enter Account Number:"))
    if taccno in d.keys():
        tpw=input("Enter Password:")
        if tpw==d[taccno][2]:
            print("Your Current Balance:",d[taccno][3])
            tamount=int(input("Enter Amount To Be Deposited:"))
            d[taccno][3]+=tamount
            print("Amount Deposited")
        else:
            print("Password Is Wrong")
    else:
        print("This Account Number Does Not Exist")
    a.close()
    return(d)
#--------------------------------------------------
def ma():
    a=open('BANK.dat','rb')
    d=p.load(a)
    taccno=int(input("Enter Account Number:"))
    if taccno in d.keys():
        tpw=input("Enter Password:")
        if tpw==d[taccno][2]:
            print("Select The Things You Want To Modify:")
            print("1.Name\n2.Password\n3.Type(Current/Savings)")
            choice=int(input())
            if choice==1:
                tname=input("Enter New Name:")
                d[taccno][1]=tname
                print("Name Modified")
            elif choice==2:
                npw=input("Enter New Password:")
                d[taccno][2]=npw
                print("Password Modified")
            else:
                if d[taccno][0]==1:
                    d[taccno][0]=2
                    print("Type Changed From Current To Savings")
                else:
                    d[taccno][0]=1
                    print("Type Changed From Savings To Current")
        else:
            print("Password Is Wrong")
    else:
        print("This Account Number Does Not Exist")
    a.close()
    return(d)
#--------------------------------------------------
def disp():
    a=open('BANK.dat','rb')
    r=p.load(a)
    print(r)
    a.close()
#--------------------------------------------------
while True:
    print("1.Create Account\n2.Delete Account\n3.Withdraw Money\n4.Deposit Money\n5.Modify Account\n6.Display\n7.Exit")
    ch=int(input())
    if ch==1:
        input_rec()
    elif ch==2:
        h=da()
        chname(h)
    elif ch==3:
        v=wm()
        chname(v)
    elif ch==4:
        q=dm()
        chname(q)
    elif ch==5:
        x=ma()
        chname(x)
    elif ch==6:
        disp()
    else:
        break
