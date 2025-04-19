import tkinter as tk
from tkinter import Entry, Frame, Button

root=tk.Tk()

root.title("On-Screen-Keyboard")
root.geometry("1400x500")
root.config(background="blue")

ent=Entry(root,width=240)
ent.grid(row=0,column=0,columnspan=80,ipady=20)
ent.config(font=("verdana",20,"bold"))

bt=Button(root,text="1")
bt.grid(row=2,column=0)
bt.config(font=("verdana",10,"bold"))

bt1=Button(root,text="2")
bt1.grid(row=2,column=1)
bt1.config(font=("verdana",10,"bold"))

bt2=Button(root,text="3")
bt2.grid(row=2,column=2)
bt2.config(font=("verdana",10,"bold"))

bt3=Button(root,text="4")
bt3.grid(row=2,column=3)
bt3.config(font=("verdana",10,"bold"))

bt4=Button(root,text="5")
bt4.grid(row=2,column=4,padx=5,pady=5)
bt4.config(font=("verdana",10,"bold"))

bt5=Button(root,text="6")
bt5.grid(row=2,column=5,padx=5,pady=5)
bt5.config(font=("verdana",10,"bold"))

bt6=Button(root,text="7")
bt6.grid(row=2,column=6,padx=5,pady=5)
bt6.config(font=("verdana",10,"bold"))

bt7=Button(root,text="8")
bt7.grid(row=2,column=7,padx=5,pady=5)
bt7.config(font=("verdana",10,"bold"))

bt8=Button(root,text="9")
bt8.grid(row=2,column=8,padx=5,pady=5)
bt8.config(font=("verdana",10,"bold"))

bt9=Button(root,text="0")
bt9.grid(row=2,column=9,padx=5,pady=5)
bt9.config(font=("verdana",10,"bold"))

bt10=Button(root,text="-")
bt10.grid(row=2,column=10,padx=1,pady=5)
bt10.config(font=("verdana",10,"bold"))

bt1=Button(root,text="=")
bt1.grid(row=2,column=11)
bt1.config(font=("verdana",10,"bold"))

bt2=Button(root,text="backspace")
bt2.grid(row=2,column=12)
bt2.config(font=("verdana",10,"bold"))

bt3=Button(root,text="+")
bt3.grid(row=2,column=13)
bt3.config(font=("verdana",10,"bold"))

bt4=Button(root,text="-")
bt4.grid(row=2,column=14,padx=5,pady=5)
bt4.config(font=("verdana",10,"bold"))

bt5=Button(root,text="NumLk")
bt5.grid(row=2,column=15,padx=5,pady=5)
bt5.config(font=("verdana",10,"bold"))




bt=Button(root,text="1")
bt.grid(row=3,column=0)
bt.config(font=("verdana",10,"bold"))

bt1=Button(root,text="3")
bt1.grid(row=3,column=1)
bt1.config(font=("verdana",10,"bold"))

bt3=Button(root,text="3")
bt3.grid(row=3,column=2)
bt3.config(font=("verdana",10,"bold"))

bt3=Button(root,text="4")
bt3.grid(row=3,column=3)
bt3.config(font=("verdana",10,"bold"))

bt4=Button(root,text="5")
bt4.grid(row=3,column=4,padx=5,pady=5)
bt4.config(font=("verdana",10,"bold"))

bt5=Button(root,text="6")
bt5.grid(row=3,column=5,padx=5,pady=5)
bt5.config(font=("verdana",10,"bold"))

bt6=Button(root,text="7")
bt6.grid(row=3,column=6,padx=5,pady=5)
bt6.config(font=("verdana",10,"bold"))

bt7=Button(root,text="8")
bt7.grid(row=3,column=7,padx=5,pady=5)
bt7.config(font=("verdana",10,"bold"))

bt8=Button(root,text="9")
bt8.grid(row=3,column=8,padx=5,pady=5)
bt8.config(font=("verdana",10,"bold"))

bt9=Button(root,text="0")
bt9.grid(row=3,column=9,padx=5,pady=5)
bt9.config(font=("verdana",10,"bold"))

bt10=Button(root,text="-")
bt10.grid(row=3,column=10,padx=1,pady=5)
bt10.config(font=("verdana",10,"bold"))

bt1=Button(root,text="=")
bt1.grid(row=3,column=11)
bt1.config(font=("verdana",10,"bold"))

bt3=Button(root,text="backspace")
bt3.grid(row=3,column=12)
bt3.config(font=("verdana",10,"bold"))

bt3=Button(root,text="+")
bt3.grid(row=3,column=13)
bt3.config(font=("verdana",10,"bold"))

bt4=Button(root,text="-")
bt4.grid(row=3,column=14,padx=5,pady=5)
bt4.config(font=("verdana",10,"bold"))

bt5=Button(root,text="NumLk")
bt5.grid(row=3,column=15,padx=5,pady=5)
bt5.config(font=("verdana",10,"bold"))




bt=Button(root,text="1")
bt.grid(row=4,column=0)
bt.config(font=("verdana",10,"bold"))

bt1=Button(root,text="4")
bt1.grid(row=4,column=1)
bt1.config(font=("verdana",10,"bold"))

bt4=Button(root,text="4")
bt4.grid(row=4,column=2)
bt4.config(font=("verdana",10,"bold"))

bt4=Button(root,text="4")
bt4.grid(row=4,column=3)
bt4.config(font=("verdana",10,"bold"))

bt4=Button(root,text="5")
bt4.grid(row=4,column=4,padx=5,pady=5)
bt4.config(font=("verdana",10,"bold"))

bt5=Button(root,text="6")
bt5.grid(row=4,column=5,padx=5,pady=5)
bt5.config(font=("verdana",10,"bold"))

bt6=Button(root,text="7")
bt6.grid(row=4,column=6,padx=5,pady=5)
bt6.config(font=("verdana",10,"bold"))

bt7=Button(root,text="8")
bt7.grid(row=4,column=7,padx=5,pady=5)
bt7.config(font=("verdana",10,"bold"))

bt8=Button(root,text="9")
bt8.grid(row=4,column=8,padx=5,pady=5)
bt8.config(font=("verdana",10,"bold"))

bt9=Button(root,text="0")
bt9.grid(row=4,column=9,padx=5,pady=5)
bt9.config(font=("verdana",10,"bold"))

bt10=Button(root,text="-")
bt10.grid(row=4,column=10,padx=1,pady=5)
bt10.config(font=("verdana",10,"bold"))

bt1=Button(root,text="=")
bt1.grid(row=4,column=11)
bt1.config(font=("verdana",10,"bold"))

bt4=Button(root,text="backspace")
bt4.grid(row=4,column=12)
bt4.config(font=("verdana",10,"bold"))

bt4=Button(root,text="+")
bt4.grid(row=4,column=13)
bt4.config(font=("verdana",10,"bold"))

bt4=Button(root,text="-")
bt4.grid(row=4,column=14,padx=5,pady=5)
bt4.config(font=("verdana",10,"bold"))

bt5=Button(root,text="NumLk")
bt5.grid(row=4,column=15,padx=5,pady=5)
bt5.config(font=("verdana",10,"bold"))



bt=Button(root,text="1")
bt.grid(row=5,column=0)
bt.config(font=("verdana",10,"bold"))

bt1=Button(root,text="5")
bt1.grid(row=5,column=1)
bt1.config(font=("verdana",10,"bold"))

bt5=Button(root,text="5")
bt5.grid(row=5,column=2)
bt5.config(font=("verdana",10,"bold"))

bt5=Button(root,text="5")
bt5.grid(row=5,column=3)
bt5.config(font=("verdana",10,"bold"))

bt5=Button(root,text="5")
bt5.grid(row=5,column=4,padx=5,pady=5)
bt5.config(font=("verdana",10,"bold"))

bt5=Button(root,text="6")
bt5.grid(row=5,column=5,padx=5,pady=5)
bt5.config(font=("verdana",10,"bold"))

bt6=Button(root,text="7")
bt6.grid(row=5,column=6,padx=5,pady=5)
bt6.config(font=("verdana",10,"bold"))

bt7=Button(root,text="8")
bt7.grid(row=5,column=7,padx=5,pady=5)
bt7.config(font=("verdana",10,"bold"))

bt8=Button(root,text="9")
bt8.grid(row=5,column=8,padx=5,pady=5)
bt8.config(font=("verdana",10,"bold"))

bt9=Button(root,text="0")
bt9.grid(row=5,column=9,padx=5,pady=5)
bt9.config(font=("verdana",10,"bold"))

bt10=Button(root,text="-")
bt10.grid(row=5,column=10,padx=1,pady=5)
bt10.config(font=("verdana",10,"bold"))

bt1=Button(root,text="=")
bt1.grid(row=5,column=11)
bt1.config(font=("verdana",10,"bold"))

bt5=Button(root,text="backspace")
bt5.grid(row=5,column=12)
bt5.config(font=("verdana",10,"bold"))

bt5=Button(root,text="+")
bt5.grid(row=5,column=13)
bt5.config(font=("verdana",10,"bold"))

bt5=Button(root,text="-")
bt5.grid(row=5,column=14,padx=5,pady=5)
bt5.config(font=("verdana",10,"bold"))

bt5=Button(root,text="NumLk")
bt5.grid(row=5,column=15,padx=5,pady=5)
bt5.config(font=("verdana",10,"bold"))




root.mainloop()