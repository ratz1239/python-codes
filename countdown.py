import time
import os as o
clrscr=lambda:o.system('cls')
def countdown(t):
    while t:
        mins,secs=divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer)
        
        time.sleep(1)
        t-=1
        clrscr()
    print("Blast Offf!!!")

t=int(input("Enter Time In Seconds:"))
countdown(t)
