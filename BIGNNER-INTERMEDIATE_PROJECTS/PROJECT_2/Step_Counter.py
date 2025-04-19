# STEP COUNTER

goal=int(input("Enter ur daily step goal:"))
take=int(input("How many step u achieve:"))
achieve=abs(goal-take)
if goal >take:
    print("You need", achieve,"step for acheive ur goal " )
elif goal<take:
    print("Congratulation u achieve ur goal and exced",achieve,"goals extra")
else:
    print("Congratulation u achieve ur goal")