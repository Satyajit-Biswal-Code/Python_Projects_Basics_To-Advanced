import random

inp="y"
while inp=="y" or inp=="Y":
    num=random.randint(1,6)

    if num== 1:
        print("[   ]\n[ 0 ]\n[   ]")

    elif num== 2:
        print("[0   ]\n[    ]\n[   0]")

    elif num== 3:
        print("[0  ]\n[ 0 ]\n[  0]")
    
    elif num== 4:
            print("[0  0]\n[    ]\n[0  0]")
    
    elif num== 5:
            print("[0  0]\n[  0 ]\n[0  0]")
    
    else:
            print("[0 0 0]\n[0 0 0]\n[0 0 0]")

    inp=input("Roll again?y/n ")

    if inp=="n" or inp=="N":
        print("Thanks for playing")
        break

else:
    print("Invalid input")
     