import tkinter as tk
from tkinter import Entry
from pyexpat.errors import messages

root=tk.Tk()

def cc():
    mail=inp.get()
    pas=inp2.get()
    if mail=="banty@gmail.com" and pas=="1234":
        print("Login")
    else:
        print("Error")

root.title("Login")
root.config(background="blue")
root.geometry("500x500")

label1=tk.Label(root,text="LOGIN HERE",bg="blue" ,fg="white")
label1.pack(pady=20)

label2=tk.Label(root,text="Enter ur email",bg="blue" ,fg="white")
label2.pack(pady=10)

inp=tk.Entry(root,width=50)
inp.pack(pady=2)

label3=tk.Label(root,text="Enter ur password",bg="blue" ,fg="white")
label3.pack(pady=10)

inp2=tk.Entry(root,width=50)
inp2.pack(pady=2)

btn=tk.Button(root,text="Login",width=20 ,command=cc)
btn.pack(pady=25)

root.mainloop()