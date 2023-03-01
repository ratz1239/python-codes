import os as o
import random as r
import time

clrscr=lambda:o.system('cls')
#-------------------------------------------------------------------------
def countdown():
    t=5
    while t:
        mins,secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t-=1
    print("GAME STARTS")
#-------------------------------------------------------------------------
def game(ans,q,b):
    print(q)
    c=l[ans-1]
    if c==q:
        print("Match Draw")
        print("Your Money Returned:",b)
    elif ans==1:
        if q=="Scissors":
            print("You Win")
            print("Bet Money Doubled:",2*b)
        else:
            print("You Lose")
            print("Bet Money Lost:",b)
    elif ans==2:
        if q=="Rock":
            print("You Win")
            print("Money Doubled:",2*b)
        else:
            print("You Lose")
            print("Bet Money Lost:",b)
    elif ans==3:
        if q=="Paper":
            print("You Win")
            print("Money Doubled:",2*b)
        else:
            print("You Lose")
            print("Bet Money Lost:",b)
    else:
        print("Invalid Input")
#-------------------------------------------------------------------------
l=["Rock","Paper","Scissors"]
while True:
    clrscr()
    print("######################### ROCK PAPER SCISSORS #########################")
    time.sleep(2)
    print("Game Starts In:-")
    countdown()
    time.sleep(2)
    b=int(input("Enter Your Bet(Min. 100):"))
    print("1.Rock\n2.Paper\n3.Scissors")
    ans=int(input())
    q=r.choice(l)
    game(ans,q,b)
    print("Do You Want To Continue(Y/N):")
    c=input()
    if c=='Y' or c=='y':
        continue
    else:
        break
