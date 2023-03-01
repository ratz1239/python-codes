import os as o
import random as r

#-----------------------------------------------------------------------------
def game(m,p):
    global l
    l[p]=m
#-----------------------------------------------------------------------------
def struct(m):
    global l
    print("Where Do You Want To Put Your Mark:")
    for i in range(0,len(l)):
        if i%6==0:
            print("\n")    
        else:
            print(l[i],end="")
    ch=int(input("\n"))
    if ch in l:
        p=l.index(ch)
    game(m,p)        
#-----------------------------------------------------------------------------
m1="O"
m2="X"
l=['_',1,'_|_',2,'_|_',3,'__',4,'_|_',5,'_|_',6,'_ ',7,' | ',8,' | ',9]
while True:
    print("                              Player 1 Turn                              ")
    struct(m1)
    if m1 is l[1] and m1 is l[9] and m1 is l[17]:
        print("############################ Player 1 Is Winner!!! ############################")
        break
    elif m1 is l[3] and m1 is l[9] and m1 is l[15]:
        print("############################ Player 1 Is Winner!!! ############################")
        break
    elif m1 is l[5] and m1 is l[9] and m1 is l[13]:
        print("############################ Player 1 Is Winner!!! ############################")
        break
    elif m1 is l[7] and m1 is l[9] and m1 is l[11]:
        print("############################ Player 1 Is Winner!!! ############################")
        break
    elif m1 is l[13] and m1 is l[15] and m1 is l[17]:
        print("############################ Player 1 Is Winner!!! ############################")
        break
    elif m1 is l[1] and m1 is l[3] and m1 is l[15]:
        print("############################ Player 1 Is Winner!!! ############################")
        break
    elif m1 is l[1] and m1 is l[7] and m1 is l[13]:
        print("############################ Player 1 Is Winner!!! ############################")
        break
    elif m1 is l[5] and m1 is l[11] and m1 is l[17]:
        print("############################ Player 1 Is Winner!!! ############################")
        break
    print("                              Player 2 Turn                              ")
    struct(m2)
    if m2 is l[1] and m2 is l[9] and m2 is l[17]:
        print("############################ Player 2 Is Winner!!! ############################")
        break
    elif m2 is l[3] and m2 is l[9] and m2 is l[15]:
        print("############################ Player 2 Is Winner!!! ############################")
        break
    elif m2 is l[5] and m2 is l[9] and m2 is l[13]:
        print("############################ Player 2 Is Winner!!! ############################")
        break
    elif m2 is l[7] and m2 is l[9] and m2 is l[11]:
        print("############################ Player 2 Is Winner!!! ############################")
        break
    elif m2 is l[13] and m2 is l[15] and m2 is l[17]:
        print("############################ Player 2 Is Winner!!! ############################")
        break
    elif m2 is l[1] and m2 is l[3] and m2 is l[15]:
        print("############################ Player 2 Is Winner!!! ############################")
        break
    elif m2 is l[1] and m2 is l[7] and m2 is l[13]:
        print("############################ Player 2 Is Winner!!! ############################")
        break
    elif m2 is l[5] and m2 is l[11] and m2 is l[17]:
        print("############################ Player 2 Is Winner!!! ############################")
        break
