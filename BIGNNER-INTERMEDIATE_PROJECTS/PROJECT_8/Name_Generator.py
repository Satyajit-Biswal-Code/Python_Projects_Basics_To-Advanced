#NAME GENERATOR
import random
from itertools import count

firstname=["Satya","Banty","Biswajit","Prakash","Abhi","Nandan","Shayam","Jagan"]
lastname=["Biswal","Sahu","Dash","Das","Khatua","Guin","Barik"]

while True:
    count=int(input("How Many name u want:"))

    for i in range(count):
        first=random.choice(firstname)
        last=random.choice(lastname)
        print(f"{first} {last}")