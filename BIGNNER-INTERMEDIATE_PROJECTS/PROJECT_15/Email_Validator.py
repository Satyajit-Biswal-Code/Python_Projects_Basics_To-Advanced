#EMAIL VALIDATOR

while True:
    email=input("Enter your Email:")

    if ( "@" in email) and ( "." in email):
        print("Valid Email")
    else:
        print("Invalid")
