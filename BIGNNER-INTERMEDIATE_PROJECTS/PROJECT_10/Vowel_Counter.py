#VOWEL COUNTER
from itertools import count

sentence=input("Enter ur word/Sentence:")
count=0

for letter in sentence:
    if letter in ["a","e","i,""o","u","A","E","I","O","U"]:
        count=count+1

print(count)