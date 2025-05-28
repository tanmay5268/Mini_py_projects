import time
import os 
#---------------------
def countdown(t):
    while t>=0:
        minutes,seconds=divmod(t,60)
        print(f"[{minutes}:{seconds}]",end= '\r')
        time.sleep(1)
        t-=1
#---------------------
timeer  = input("enter time in seconds")
os.system("clear")
countdown(int(timeer))