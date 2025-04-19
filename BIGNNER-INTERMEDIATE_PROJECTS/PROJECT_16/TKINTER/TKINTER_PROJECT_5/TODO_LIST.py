import tkinter as tk
from tkinter import Entry, Button, Listbox
from tkinter import messagebox
from pyexpat.errors import messages

root=tk.Tk()

root.title("TodoList")
root.geometry("300x400")
root.maxsize(300,500)
root.minsize(300,500)
root.config(background="blue")

def add():
    if entt.get() =="":
        messagebox.showwarning("Warning", "Please enter your todo")
    else:
        data=str(entt.get())
        print(str(data))
        listb.insert(tk.END,data)
        entt.delete(0,tk.END)

def dele():
    print("Delete")
    selected=listb.curselection()
    listb.delete(selected)


entt=Entry(width=50)
entt.pack(pady=20,ipady=5)
entt.config(font=("sans",10,"bold"))

add=Button(root,text="Add",command=add)
add.pack()

add=Button(root,text="Delete",command=dele)
add.pack(pady=5)


listb=Listbox(root,width=30,height=20)
listb.pack(padx=60)




root.mainloop()