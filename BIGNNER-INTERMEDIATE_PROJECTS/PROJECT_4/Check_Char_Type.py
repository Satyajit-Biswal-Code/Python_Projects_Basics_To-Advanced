# CHECK CHAR TYPE

char=input("Enter ur words/Sentences:")

if char.isalpha():
    print("It is an alphabet")
elif char.isdigit():
    print("It is a number")
else:
    print("It is a special character")