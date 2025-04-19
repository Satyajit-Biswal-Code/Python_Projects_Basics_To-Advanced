#COUNTDOWN TIMER
import time
from secrets import choice

while True:
    timee=int(input("Enter ur counts:"))

    for i in range(timee,0,-1):
        print(f"{i} time remaining........")
        time.sleep(1)

    need=input("If u try or not y/n")
    if need.lower() != "y":
        break

