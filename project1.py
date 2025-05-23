#NUMBER GUESSING GAME :-)
import random
x=int(input("ENTER lower bound"))
y = int(input("Enter upper bound"))
target = random.randint(x,y)
chance=4
while chance>0:
    guess=int(input("ENTER YOUR GUESS"))
    if guess ==target:
        print(f"YOU WON!!! \n number is:{guess}")
        break
    elif guess>target:
        print("Try some low numbers")
    elif guess<target:
        print("try some higher number")
    elif chance==1 and guess!=target:
        print("YOU FAILED")
    print(f"you have {chance-1} guesses left")
    chance -= 1
    
