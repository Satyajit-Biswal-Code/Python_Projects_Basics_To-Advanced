#REVERSE NAME

print("Name Generator")
while True:
    name=input("Enter Ur name:")
    rev_name=name[::-1]
    print(rev_name)

    answer=input("Try new name?(y/n)")
    if answer !="y":
        break