import pickle as p
import os as o

d={}
count=0

def createrec():
#------------------------------------------
    
def deleterec():
#------------------------------------------
    
def modrec():
#------------------------------------------
    
def searchrec():
#------------------------------------------
    
def disprec():
#------------------------------------------

while True:
    print("1.Create\n2.Delete\n3.Modify\n4.Search\n5.Display\n6.Exit")
    ch=int(input())
    if ch is 1:
        createrec()
    elif ch is 2:
        deleterec()
    elif ch is 3:
        modrec()
    elif ch is 4:
        searchrec()
    elif ch is 5:
        disprec()
