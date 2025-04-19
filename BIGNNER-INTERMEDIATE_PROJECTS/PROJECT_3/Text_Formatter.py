# TEXT FORMATTER

text=str(input("Enter ur words/Sentences:"))
print("1.UPPER CASE")
print("2.lower case")
print("3.Title Case")
print("4.Sentence case")

press=int(input("Enter u change ur word to following formatter,press 1-4:"))

if press==1:
    print(text.upper())
elif press==2:
    print(text.lower())
elif press==3:
    print(text.title())
elif press==4:
    print(text.capitalize())
else:
    print("Please Press valid no. for operations")