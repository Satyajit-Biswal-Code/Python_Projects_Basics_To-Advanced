import tkinter as tk
from tkinter import Entry, Label, Button, StringVar

root=tk.Tk()
root.resizable(0,0)
root.title("Calculator")
root.config(background="blue")
v=StringVar()
a=" "
op=" "
def click(x):
    global a
    global op
    a=a+str(x)
    v.set(a)
    op=eval(a)

def clr():
    show.delete(0,tk.END)
    global a
    a=" "

def final():
    global op
    v.set(op)

show=Entry(root,textvariable=v)
show.grid(row=1,column=1,columnspan=4,pady=20,ipady=10)
show.config(font=("verdana",20,"bold"))

bt1=Button(root,text="7",command=lambda:click(7))
bt1.config(font=("verdana",20,"bold"))
bt1.grid(row=2,column=1,)


bt2=Button(root,text="8",command=lambda:click(8))
bt2.config(font=("verdana",20,"bold"))
bt2.grid(row=2,column=2)


bt3=Button(root,text="9",command=lambda:click(9))
bt3.config(font=("verdana",20,"bold"))
bt3.grid(row=2,column=3, padx=5, pady=5)


bt4=Button(root,text="+",command=lambda:click("+"))
bt4.config(font=("verdana",20,"bold"),relief="raised")
bt4.grid(row=2,column=4, padx=5, pady=5)


bt5=Button(root,text="4",command=lambda:click(4))
bt5.config(font=("verdana",20,"bold"))
bt5.grid(row=3,column=1,)


bt6=Button(root,text="5",command=lambda:click(5))
bt6.config(font=("verdana",20,"bold"))
bt6.grid(row=3,column=2, padx=5, pady=5)


bt7=Button(root,text="6",command=lambda:click(6))
bt7.config(font=("verdana",20,"bold"))
bt7.grid(row=3,column=3, padx=5, pady=5)


bt8=Button(root,text="-",command=lambda :click("-"))
bt8.config(font=("verdana",20,"bold"),relief="raised")
bt8.grid(row=3,column=4, padx=5, pady=5)


bt9=Button(root,text="3",command=lambda:click(3))
bt9.config(font=("verdana",20,"bold"))
bt9.grid(row=4,column=1, padx=5, pady=5)


bt10=Button(root,text="2",command=lambda:click(2))
bt10.config(font=("verdana",20,"bold"))
bt10.grid(row=4,column=2, padx=5, pady=5)


bt11=Button(root,text="1",command=lambda:click(1))
bt11.config(font=("verdana",20,"bold"))
bt11.grid(row=4,column=3, padx=5, pady=5)


bt12=Button(root,text="*",command=lambda :click("*"))
bt12.config(font=("verdana",20,"bold"),relief="raised")
bt12.grid(row=4,column=4, padx=5, pady=5)



bt13=Button(root,text="C",command=lambda:clr())
bt13.config(font=("verdana",20,"bold"))
bt13.grid(row=5,column=1, padx=5, pady=5)


bt14=Button(root,text="0",command=lambda:click(0))
bt14.config(font=("verdana",20,"bold"))
bt14.grid(row=5,column=2, padx=5, pady=5)


bt15=Button(root,text="=",command=lambda :final())
bt15.config(font=("verdana",20,"bold"))
bt15.grid(row=5,column=3, padx=5, pady=5)


bt16=Button(root,text="/",command=lambda :click("/"))
bt16.config(font=("verdana",20,"bold"),relief="raised")
bt16.grid(row=5,column=4, padx=5, pady=5)




root.mainloop()

