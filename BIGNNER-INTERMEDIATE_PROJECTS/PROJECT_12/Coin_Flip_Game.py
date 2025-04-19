#COIN FLIP GAME
import random

while True:
    call=input("Enter ur call Head/Tail:")
    toss=random.choice(["head","tail"])
    if toss== "head":
        print("Head")
    else:
        print("Tail")

    if call.lower()==toss:
        print("You Win")
    else:
        print("You Loss")

    ans=input("Try again?(y/n):")

    if ans !="y":
        break