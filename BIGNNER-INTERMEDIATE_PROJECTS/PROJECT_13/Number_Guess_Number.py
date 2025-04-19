import random 

l=True
num=random.randint(1,100)
inp=int(input("Enter a number between 1 and 100: "))
while l:
    if inp >num:
        
        print("Your Number is Larger Than Computer number")
        inp=int(input("Enter a number between 1 and 100: "))
    elif inp < num:
        
        print("Your Number is Smaller Than Computer Number")
        inp=int(input("Enter a number between 1 and 100: "))
    
    else:
        print("You Guess The Correct Number")
        print("Finally U have Successfully Guessed the Number")
        l=False
        