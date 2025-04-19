# WEBSITE URL CHECKER

url=input("Enter ur website URL:")

if url.startswith("https")  :
    print("This website is Secure")
elif url.startswith("http") :
    print("This website is Not Secure")
else:
    print("It is not a website")
