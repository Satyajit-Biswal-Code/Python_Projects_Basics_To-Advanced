# GRADE CONVERTOR


while True:
    score=input("Enter ur score:")

    if score.lower()=="done":
        print("Ok")
    elif score>="90":
        print("A grade")
    elif score>="80":
        print("B grade")
    elif score>="70":
        print("C grade")
    elif score>="60":
        print("D grade")
    elif score>"40":
        print("Average mark")
    else:
        print("Fail")