import tkinter as tk
import datetime
from tkinter.ttk import Label

from click import command

root=tk.Tk()
root.geometry("400x300")
root.config(background="blue")

def show_time():
    time=datetime.datetime.now()
    hr=time.strftime("%I")
    mint=time.strftime("%M")
    sec=time.strftime("%S")
    lab_hr.config(text=hr)
    lab_mint.config(text=mint)
    lab_sec.config(text=sec)
    lab_hr.after(200,show_time)



label=Label(root,text="Digital Clock")
label.config(font=("verdana",20))
label.grid(row=0,column=3,columnspan=4,padx=10,pady=10)

lab_hr=Label(root,text="00")
lab_hr.config(font=("verdana",20))
lab_hr.grid(row=1,column=1,padx=20,pady=20)

lab_mint=Label(root,text="00")
lab_mint.config(font=("verdana",20))
lab_mint.grid(row=1,column=3,padx=20,pady=20)

lab_sec=Label(root,text="00")
lab_sec.config(font=("verdana",20))
lab_sec.grid(row=1,column=5,padx=20,pady=20)


hour=Label(root,text="Hours")
hour.config(font=("verdana",10))
hour.grid(row=2,column=1,padx=20,pady=5)

mintt=Label(root,text="Minutes")
mintt.config(font=("verdana",10))
mintt.grid(row=2,column=3,padx=20,pady=5)

secc=Label(root,text="Seconds")
secc.config(font=("verdana",10))
secc.grid(row=2,column=5,padx=20,pady=5)

show_time()

root.mainloop()