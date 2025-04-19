# WORD SCRAMBLER
# WE TAKE A WORD AND CONVERT TO ANOTHER WORD OF SAME WORD WHICH DO NOT HAVE ANY MEANING THAT IS WORD SCRAMBLER.

import random
c=True
while c:
    word = input("Enter ur Word:")
    if word.lower()=="quit":
        print("Good Bye")
        break
    letter=list(word)
    random.shuffle(letter)
    print("".join(letter))