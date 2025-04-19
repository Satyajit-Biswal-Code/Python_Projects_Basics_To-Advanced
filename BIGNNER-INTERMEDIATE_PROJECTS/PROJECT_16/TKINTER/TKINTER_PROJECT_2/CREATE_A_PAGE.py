import tkinter as tk
from tkinter import Label, Entry, Button, Frame
from tkinter.constants import BOTTOM

root=tk.Tk()
root.geometry("500x500")
root.maxsize(500,500)
root.minsize(500,500)
root.config(background="#90ee90")
root.title("Whatsapp")
root.iconbitmap("wp.png")

def sub():
    print("sub")

def clr():
    print("clr")
    ent.delete(0, tk.END)
    ent1.delete(0, tk.END)


label=Label(root,text="Whatsapp\n web",fg="white",bg="red")
label.grid(row=1,column=0,pady=50,padx=100)

label2=Label(root,text="Image",fg="white",bg="red")
label2.grid(row=1,column=1,pady=50,padx=100)

label3=Label(root,text="Username:")
label3.grid(row=3,column=0,pady=30,ipadx=4,ipady=5)

ent=tk.Entry(width=30)
ent.grid(row=3,column=1,pady=30,ipadx=4,ipady=5)

label4=Label(root,text="Password:")
label4.grid(row=4,column=0,padx=30,pady=10,ipadx=4,ipady=5)

ent1=tk.Entry(width=30)
ent1.grid(row=4,column=1,ipadx=4,ipady=5)


btn=Button(root,text="Submit",width=10,command=sub)
btn.grid(row=5,column=0,pady=20,padx=20)

btn1=Button(root,text="Clear",width=10,command=clr)
btn1.grid(row=5,column=1,pady=20,padx=20)


topep=Frame(root)
topep.grid()

label5=Label(topep,text="Banty")
label5.pack(side="bottom")

root.mainloop()